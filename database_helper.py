from pymongo import MongoClient
import os
import json


class Database:
    MONGO_ADDRESS = 'localhost'
    MONGO_PORT = 27017
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            data = json.load(file)
            MONGO_ADDRESS = data["address"]
            MONGO_PORT = data["port"]

    def __init__(self, db_name="recipe_db", recipe_collection_name="recipes", ingredient_collection_name="ingredients"):
        # Connect to the local MongoDB instance
        self.connect_to_db()
        

    def connect_to_db(self):
        self.client = MongoClient(Database.MONGO_ADDRESS, Database.MONGO_PORT)
        self.db = self.client["recipe_db"]
        self.collection = self.db["recipes"]
        self.ingredient_collection = self.db["ingredients"]

        



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
        return self.collection.find_one({"recipe_name": recipe_name})
    def get_all_recipes(self):
        """
        Fetch all recipes.
        """
        return self.collection.find({})

    def filter_recipes(self, filter_type, selected_ingredients):
        """
        Filter recipes based on type and selected ingredients.
        """
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
        return self.ingredient_collection.insert_one({"name": ingredient_name}).inserted_id

    def get_all_ingredients(self):
        """
        Fetch all ingredients.
        """
        return [ingredient['name'] for ingredient in self.ingredient_collection.find({})]
    def remove_ingredient(self, ingredient_name):
        """Remove an ingredient from the database."""
        self.ingredient_collection.delete_one({"name": ingredient_name})
    @classmethod
    def update_connection(cls, address, port):
        """Update the MongoDB connection details."""
        cls.MONGO_ADDRESS = address
        cls.MONGO_PORT = port
        

        
