import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QDialog, 
                               QVBoxLayout, QLabel, QLineEdit, QPushButton, 
                               QMessageBox)
from createRecipe import CreateRecipe
from readRecipe import ReadRecipe
from settings import SettingsApplet
from database_helper import Database

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipe App")
        self.setGeometry(100, 100, 950, 825)

        self.db = Database()
        if self.db.connection_status:
            self.init_ui_with_tabs()
        else:
            self.show_connection_popup()

    def init_ui_with_tabs(self):
        self.central_widget = QTabWidget()
        self.setCentralWidget(self.central_widget)

        # Create three tabs for the applets
        self.applet1 = CreateRecipe()
        self.applet2 = ReadRecipe()
        self.applet3 = SettingsApplet()

        self.central_widget.addTab(self.applet1, "Create Recipe")
        self.central_widget.addTab(self.applet2, "Read Recipe")
        self.central_widget.addTab(self.applet3, "Settings")

    def show_connection_popup(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Connection Error")
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Failed to connect to the database. Please provide connection details:"))
        
        address_label = QLabel("Address:")
        address_input = QLineEdit()
        layout.addWidget(address_label)
        layout.addWidget(address_input)

        port_label = QLabel("Port:")
        port_input = QLineEdit()
        layout.addWidget(port_label)
        layout.addWidget(port_input)

        buttons_layout = QHBoxLayout()
        
        save_button = QPushButton("Save & Continue")
        save_button.clicked.connect(lambda: self.try_connect(address_input.text(), port_input.text(), dialog))
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(sys.exit)
        
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(cancel_button)

        layout.addLayout(buttons_layout)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def try_connect(self, address, port, dialog):
        success = self.db.update_connection(address, port)
        if success:
            dialog.close()
            self.init_ui_with_tabs()
        else:
            QMessageBox.warning(self, "Connection Error", "Failed to connect with provided details. Please try again.")

def main():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
