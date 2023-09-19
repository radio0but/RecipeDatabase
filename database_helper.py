from pymongo import MongoClient
import os
import json
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from pymongo.errors import ServerSelectionTimeoutError
import sys



class Database:
    MONGO_ADDRESS = 'localhost'
    MONGO_PORT = 27017
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            data = json.load(file)
            MONGO_ADDRESS = data["address"]
            MONGO_PORT = data["port"]

    def __init__(self, db_name="recipe_db", recipe_collection_name="recipes", ingredient_collection_name="ingredients"):
        
        self.db_name = db_name
        self.recipe_collection_name = recipe_collection_name  # <-- Add this line
        self.ingredient_collection_name = ingredient_collection_name  # <-- Add this line

        # Connect to the local MongoDB instance
        self.connection_status = False
        try:
            self.connect_to_db()
            self.connection_status = True
        except Exception as e:
            print(f"Failed to connect to database: {e}")

    def connect_to_db(self):
        retries = 3
        while retries:
            try:
                self.client = MongoClient(Database.MONGO_ADDRESS, Database.MONGO_PORT)
                self.db = self.client[self.db_name]
                self.collection = self.db["recipes"]
                self.ingredient_collection = self.db["ingredients"]
                break  # If no error is raised, break out of the loop.
            except ServerSelectionTimeoutError:
                print(f"Connection failed. Retries left: {retries}")
                retries -= 1
        if not retries:
            print("Failed to connect to database after 3 attempts. Exiting.")
            #sys.exit(0)  # Exit the app if the connection fails after 3 attempts.

    def remove_recipe(self, recipe_name):
        recipe_collection = self.client[self.db_name][self.recipe_collection_name]
        result = recipe_collection.delete_one({"recipe_name": recipe_name})
        return result.deleted_count > 0

    def add_or_update_recipe(self, recipe_name, ingredients, steps):
        existing_recipe = self.get_recipe(recipe_name)
        recipe = {
            "recipe_name": recipe_name,
            "ingredients": ingredients,
            "steps": steps
        }
        if existing_recipe:
            self.collection.update_one({"recipe_name": recipe_name}, {"$set": recipe})
        else:
            self.collection.insert_one(recipe)
            
    def get_recipe(self, recipe_name):
        """
        Fetch a recipe by name.
        """
        if self.connection_status:
            return self.collection.find_one({"recipe_name": recipe_name})
        else:
            print("Database connection not available.")
            return None

    def filter_recipes(self, filter_type, selected_ingredients):
        """
        Filter recipes based on type and selected ingredients.
        """
        if not self.connection_status:
            print("Database connection not available.")
            return []

        if filter_type == 0:
            # Contains selected ingredients
            return self.collection.find({"ingredients": {"$all": selected_ingredients}})
        else:
            # Doesn't need other ingredients
            return [recipe for recipe in self.collection.find({}) if set(recipe["ingredients"]).issubset(set(selected_ingredients))]

    def add_ingredient(self, ingredient_name):
        """
        Add an ingredient to the ingredient collection.
        """
        if not self.connection_status:
            print("Database connection not available.")
            return None

        return self.ingredient_collection.insert_one({"name": ingredient_name}).inserted_id

    def get_all_ingredients(self):
        """
        Fetch all ingredients.
        """
        if not self.connection_status:
            print("Database connection not available.")
            return []

        return [ingredient['name'] for ingredient in self.ingredient_collection.find({})]

    def remove_ingredient(self, ingredient_name):
        """
        Remove an ingredient from the database.
        """
        if not self.connection_status:
            print("Database connection not available.")
            return

        self.ingredient_collection.delete_one({"name": ingredient_name})
    def disable_controls(self):
        self.ui.add_ingredient_button.setEnabled(False)
        self.ui.add_step_button.setEnabled(False)
        self.ui.save_button.setEnabled(False)
        self.ui.clear_button.setEnabled(False)
        self.ui.open_recipe_button.setEnabled(False)   
    def populate_recipes_dropdown(self):
        all_recipes = self.db.get_all_recipes()
        self.ui.recipes_dropdown.clear()
        for recipe in all_recipes:
            self.ui.recipes_dropdown.addItem(recipe['recipe_name'])
    def open_recipe_from_db(self):
        selected_recipe_name = self.ui.recipes_dropdown.currentText()
        recipe = self.db.get_recipe(selected_recipe_name)
        if not recipe:
            QMessageBox.warning(self, "Error", "Selected recipe not found!")
            return

        # Clear the current form
        self.clear_form()

        # Populate the form with the selected recipe's data
        self.ui.recipe_name_input.setText(recipe['recipe_name'])

        # Check the required ingredients checkboxes
        for ingredient in recipe['ingredients']:
            if ingredient in self.ingredient_widgets:
                self.ingredient_widgets[ingredient].setChecked(True)

        # Populate the steps
# Inside the open_recipe_from_db method:

        # Inside the open_recipe_from_db method:

        for step in recipe['steps']:
            self.add_step()

            # Get the last step_container added to the steps_layout
            step_container = self.ui.steps_layout.itemAt(self.ui.steps_layout.count() - 1).widget()

            # Find the QTextEdit widget inside the step_container
            text_edit = step_container.findChild(QTextEdit)
            
            text_edit.setPlainText(step) 
    def get_all_recipes(self):
        """
        Fetch all recipes.
        """
        if not self.connection_status:
            print("Database connection not available.")
            return []

        return [recipe for recipe in self.collection.find({})]
    @classmethod
    def update_connection(cls, address, port):
        """Update the MongoDB address and port and reconnect."""
        cls.MONGO_ADDRESS = address
        cls.MONGO_PORT = port

        # Try connecting using the new parameters
        db_instance = cls()
        if db_instance.connection_status:
            return True
        else:
            return False