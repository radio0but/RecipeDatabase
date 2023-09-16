from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QCoreApplication
import subprocess
import os
import json

class SettingsApplet(QWidget):
    def __init__(self):
        super().__init__()
        QCoreApplication.instance().aboutToQuit.connect(self.stop_webui)
        
        # Load the UI design
        loader = QUiLoader()
        file = QFile("settings_applet.ui")  # Adjust the path if the .ui file is located elsewhere
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        
        self.init_ui()

    def init_ui(self):

        self.ui.save_button.clicked.connect(self.save_config)
        self.ui.startWebUIButton.clicked.connect(self.start_webui)
        self.ui.stopWebUIButton.clicked.connect(self.stop_webui)
        self.ui.address_input.setText("localhost")
        self.ui.port_input.setText("27017")
        if os.path.exists("config.json"):
            with open("config.json", "r") as file:
                data = json.load(file)
                self.ui.address_input.setText(data["address"])
                self.ui.port_input.setText(str(data["port"]))


    def save_config(self):
        address = self.ui.address_input.text()
        port = int(self.ui.port_input.text())
        
        # Save address and port to config.json
        with open("config.json", "w") as file:
            json.dump({"address": address, "port": port}, file)

        # Update the database connection
        from database_helper import Database  # Avoid cyclic imports
        Database.update_connection(address, port)
        db_instance = Database()
        print(f"Address: {address}, Port: {port}")
    def closeEvent(self, event):
        self.stop_webui()
        super().closeEvent(event)

    def start_webui(self):
        self.server_process = subprocess.Popen(['python', 'webUI.py'])
        self.ui.startWebUIButton.setEnabled(False)
        self.ui.stopWebUIButton.setEnabled(True)

    def stop_webui(self):
        self.server_process.terminate()
        self.server_process.wait()  # Wait for the process to terminate
        self.ui.startWebUIButton.setEnabled(True)
        self.ui.stopWebUIButton.setEnabled(False)
