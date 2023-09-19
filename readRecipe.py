from PySide6.QtWidgets import (QWidget, QCheckBox,QVBoxLayout)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QCoreApplication
from database_helper import Database
from threading import Thread
from flask import Flask
from flask_socketio import SocketIO
from webUI import app, socketio, run_app
import requests
import subprocess

class ReadRecipe(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.connection_available = self.db.connection_status
        # Load the UI design
        loader = QUiLoader()
        file = QFile("read_recipe.ui")  # Adjust the path to your actual file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        
        # Initialize UI
        self.init_ui()


    def init_ui(self):
        # Connect the UI widgets
        self.ui.recipe_list.itemClicked.connect(self.display_recipe)
        self.ui.filter_button.clicked.connect(self.apply_filter)
        self.ui.remove_filter_button.clicked.connect(self.remove_filters)
        self.ui.refresh_button.clicked.connect(self.refresh_data)
        if self.connection_available:
            # Populate the widgets only if the connection is available
            self.populate_recipe_list()
            self.populate_ingredient_filters()
        else:
            self.disable_controls()

    def remove_filters(self):
        for checkbox in self.ingredient_filters.values():
            checkbox.setChecked(False)
        self.populate_recipe_list()

    def populate_recipe_list(self):
        self.ui.recipe_list.clear()
        if not self.connection_available:
            print("Database connection not available.")
            return
        
        recipes = self.db.collection.find({})
        for recipe in recipes:
            self.ui.recipe_list.addItem(recipe['recipe_name'])

    def display_recipe(self, item):
        if not self.connection_available:
            print("Database connection not available.")
            return

        recipe = self.db.get_recipe(item.text())
        
        # Check if the steps are in HTML format
        if any('<html>' in step for step in recipe["steps"]):
            details = "Ingredients: " + ", ".join(recipe["ingredients"]) + "<br>Steps:<br>" + "<br>".join(recipe["steps"])
        else:
            details = "Ingredients: " + ", ".join(recipe["ingredients"]) + "\nSteps:\n" + "\n".join(recipe["steps"])
                
        self.ui.recipe_details_browser.setHtml(details)  # Note: recipe_details_browser is our QTextBrowser

    def apply_filter(self):
        if not self.connection_available:
            print("Database connection not available.")
            return

        selected_ingredients = [ingredient for ingredient, checkbox in self.ingredient_filters.items() if checkbox.isChecked()]
        filter_type = self.ui.filter_dropdown.currentIndex()

        if filter_type == 0:
            recipes = self.db.collection.find({"ingredients": {"$all": selected_ingredients}})
        else:
            recipes = self.db.filter_recipes(filter_type, selected_ingredients)

        self.ui.recipe_list.clear()
        for recipe in recipes:
            self.ui.recipe_list.addItem(recipe['recipe_name'])

    def populate_ingredient_filters(self):
        if not self.connection_available:
            print("Database connection not available.")
            return

        self.ingredient_filters = {}
        
        # Create a QWidget for the QScrollArea
        scroll_area_widget_contents = QWidget()
        
        # Create a QVBoxLayout for the QWidget
        scroll_layout = QVBoxLayout(scroll_area_widget_contents)

        # Populate the QVBoxLayout with QCheckBoxes
        for ingredient in self.db.get_all_ingredients():
            checkbox = QCheckBox(ingredient)
            scroll_layout.addWidget(checkbox)
            self.ingredient_filters[ingredient] = checkbox

        # Ensure the layout expands to the size of its content.
        scroll_layout.setSizeConstraint(QVBoxLayout.SetNoConstraint)
        
        # Set the QWidget as the widget for the QScrollArea.
        self.ui.scrollArea.setWidget(scroll_area_widget_contents)
    def disable_controls(self):
        self.ui.recipe_list.setEnabled(False)
        self.ui.filter_button.setEnabled(False)
        self.ui.remove_filter_button.setEnabled(False)
        self.ui.refresh_button.setEnabled(False)

    def refresh_data(self):
        if self.connection_available:
            self.populate_recipe_list()
            self.populate_ingredient_filters()
   
    