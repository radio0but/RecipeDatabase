import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from createRecipe import CreateRecipe
from readRecipe import ReadRecipe
from settings import SettingsApplet

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipe App")
        self.setGeometry(100, 100, 861, 800)

        self.central_widget = QTabWidget()
        self.setCentralWidget(self.central_widget)

        # Create two tabs for the applets
        self.applet1 = CreateRecipe()
        self.applet2 = ReadRecipe()
        self.applet3 = SettingsApplet()

        self.central_widget.addTab(self.applet1, "Create Recipe")
        self.central_widget.addTab(self.applet2, "Read Recipe")
        self.central_widget.addTab(self.applet3, "Settings")

def main():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    recipe_reader = ReadRecipe(socketio)
