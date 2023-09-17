# Recipe App

Recipe App is a comprehensive tool designed to help users manage their recipes. The application provides an intuitive interface for creating, reading, and managing recipes. Users can also filter recipes based on specific ingredients, ensuring they always find what they're looking for. For those who prefer a web-based approach, a `webUI.py` is also provided to access and manage the recipes via a browser.

## Table of Contents
- [Installation](#installation)
  - [Dependencies](#dependencies)
  - [MongoDB Setup](#mongodb-setup)
- [Usage](#usage)
  - [Launching the App](#launching-the-app)
  - [Using Web UI](#using-web-ui)

## Installation

### Dependencies

#### Windows

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Using pip (Python package installer), install the required packages:

```
pip install PySide6 flask flask_socketio pymongo
```

#### macOS

1. Install Python using Homebrew:

```
brew install python
```

2. Install the required packages:

```
pip3 install PySide6 flask flask_socketio pymongo
```

#### Ubuntu

1. Update the package list and install Python:

```
sudo apt update
sudo apt install python3 python3-pip
```

2. Install the required packages:

```
pip3 install PySide6 flask flask_socketio pymongo
```

#### Arch Linux

1. Update the package list and install Python:

```
sudo pacman -Sy python python-pip
```

2. Install the required packages:

```
pip install PySide6 flask flask_socketio pymongo
```

#### Fedora

1. Install Python:

```
sudo dnf install python3 python3-pip
```

2. Install the required packages:

```
pip3 install PySide6 flask flask_socketio pymongo
```

### MongoDB Setup

#### Windows

1. Download the MongoDB installer from the [official website](https://www.mongodb.com/try/download/community).
2. Follow the installation wizard to install.

#### macOS

1. Use Homebrew:

```
brew tap mongodb/brew
brew install mongodb-community@5.0
```

2. Start the MongoDB server:

```
brew services start mongodb/brew/mongodb-community
```

#### Ubuntu

1. Import the public key:

```
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```

2. Create a list file for MongoDB:

```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

3. Reload local package database:

```
sudo apt update
```

4. Install MongoDB packages:

```
sudo apt install -y mongodb-org
```

5. Start MongoDB:

```
sudo systemctl start mongod
```

#### Arch Linux

1. Install MongoDB:

```
yay -S mongodb-bin
```

2. Start MongoDB:

```
sudo systemctl start mongodb
```

#### Fedora

1. Install MongoDB:

```
sudo dnf install mongodb mongodb-server
```

2. Start MongoDB:

```
sudo systemctl start mongod
```

## Usage

### Launching the App

1. Navigate to the directory containing the app.
2. Run the `main.py` file:

```
python main.py
```

- For Create Recipe Tab:
  - Fill out the recipe name, ingredients, and steps.
  - Click 'Save' to save the recipe.
  
- For Read Recipe Tab:
  - Browse through the list of available recipes.
  - Click on a recipe to view its details.
  - Use the filters to search for recipes with specific ingredients.

### Using Web UI

1. Navigate to the directory containing the `webUI.py` file.
2. Start the Flask server:

```
python webUI.py
```

3. Open a web browser and go to `http://localhost:5000` to access the web interface.
4. Browse recipes, view individual recipe details, and apply filters as needed.

---

Enjoy using Recipe App to manage and explore delightful recipes!
