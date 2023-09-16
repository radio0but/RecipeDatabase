from PySide6.QtWidgets import QWidget, QCheckBox, QTextEdit, QHBoxLayout, QPushButton, QMessageBox,QVBoxLayout,QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from database_helper import Database


class CreateRecipe(QWidget):
    def __init__(self):
        super().__init__()

        self.db = Database()

         # Initialize ingredient_widgets dictionary
        self.ingredient_widgets = {}  # Add this line

        # Load the UI design
        loader = QUiLoader()
        file = QFile("create_recipe.ui")  # Adjust the path to your actual file
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        # Initialize UI
        self.init_ui()

    def init_ui(self):

        # Bind buttons' signals to your methods
        self.ui.add_ingredient_button.clicked.connect(self.add_ingredient_to_db)
        self.ui.add_step_button.clicked.connect(self.add_step)
        self.ui.save_button.clicked.connect(self.save_recipe)
        self.ui.clear_button.clicked.connect(self.clear_form)
        self.ui.open_recipe_button.clicked.connect(self.open_recipe_from_db)


        # Populating ingredients
        self.populate_ingredients()
        self.add_step()
        self.populate_recipes_dropdown()

    def add_step(self):
        # Create a container for each step with a vertical layout
        step_container = QWidget()
        step_layout = QVBoxLayout(step_container)

        # Create a title label for the step
        step_count = self.ui.steps_layout.count() + 1
        step_title = QLabel(f"Step {step_count}")
        step_title.setStyleSheet("font-weight: bold;")  # Optional: setting the label as bold
        step_layout.addWidget(step_title)

        # Create the text edit for the step
        step_edit = QTextEdit()
        step_layout.addWidget(step_edit)

        # Add the container to the steps layout
        self.ui.steps_layout.addWidget(step_container)

    def save_recipe(self):
        recipe_name = self.ui.recipe_name_input.text()
        ingredients = [ingredient for ingredient, widget in self.ingredient_widgets.items() if widget.isChecked()]
        steps = [container.findChild(QTextEdit).toPlainText() for i in range(self.ui.steps_layout.count()) for container in [self.ui.steps_layout.itemAt(i).widget()]]

        self.db.add_or_update_recipe(recipe_name, ingredients, steps)
        self.clear_form()


    def clear_form(self):
        self.ui.recipe_name_input.clear()
        for checkbox in self.ingredient_widgets.values():
            checkbox.setChecked(False)
        for i in reversed(range(self.ui.steps_layout.count())):
            widget = self.ui.steps_layout.itemAt(i).widget()
            self.ui.steps_layout.removeWidget(widget)
            widget.deleteLater()


    def populate_ingredients(self):
        # Get the current ingredients from the database
        current_ingredients = self.db.get_all_ingredients()

        # Add only the new ones to the UI
        for ingredient in current_ingredients:
            if ingredient not in self.ingredient_widgets:
                widget = QWidget()
                layout = QHBoxLayout(widget)

                checkbox = QCheckBox(ingredient)
                remove_button = QPushButton("Remove")
                remove_button.clicked.connect(lambda checked=False, ing=ingredient: self.remove_ingredient(ing))

                layout.addWidget(checkbox)
                layout.addWidget(remove_button)
                widget.setLayout(layout)

                self.ui.ingredient_scroll_content.layout().addWidget(widget)  # Adjusted this line
                self.ingredient_widgets[ingredient] = checkbox


    def add_ingredient_to_db(self):
        ingredient_name = self.ui.new_ingredient_input.text().strip()
        if ingredient_name and ingredient_name not in self.ingredient_widgets:
            self.db.add_ingredient(ingredient_name)
            self.ui.new_ingredient_input.clear()
            self.refresh_ingredient_list()

    def refresh_ingredient_list(self):
        for ingredient, checkbox in list(self.ingredient_widgets.items()):
            ingredient_container = checkbox.parentWidget()  # Get the parent widget of the checkbox
            self.ui.ingredient_scroll_content.layout().removeWidget(ingredient_container)
            ingredient_container.deleteLater()
            del self.ingredient_widgets[ingredient]
        self.populate_ingredients()

    def remove_ingredient(self, ingredient_name):
        # Display confirmation dialog
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Confirmation")
        msgBox.setText(f"Are you sure you want to delete the ingredient '{ingredient_name}'?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        
        # Check the user's decision
        if msgBox.exec() == QMessageBox.Yes:
            # User chose 'Yes', proceed with deletion
            
            # Remove from database
            self.db.remove_ingredient(ingredient_name)

            # Remove the widget associated with this ingredient from the UI
            ingredient_widget = self.ingredient_widgets[ingredient_name].parentWidget()  # get the parent widget containing the checkbox
            self.ui.ingredient_scroll_content.layout().removeWidget(ingredient_widget)
            ingredient_widget.deleteLater()
            del self.ingredient_widgets[ingredient_name]
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


