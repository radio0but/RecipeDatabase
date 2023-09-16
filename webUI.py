from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
from database_helper import Database

from bson import json_util
import json

def mongo_to_json(data):
    return json.loads(json_util.dumps(data))


app = Flask(__name__)
socketio = SocketIO(app)
should_shutdown = False

db = Database()

@app.route('/')
def index():
    return render_template('index.html', ingredients=db.get_all_ingredients(), recipes=db.get_all_recipes())

@app.route('/recipe/<recipe_name>')
def get_recipe(recipe_name):
    recipe = db.get_recipe(recipe_name)
    sanitized_recipe = mongo_to_json(recipe)
    return jsonify(sanitized_recipe)

@socketio.on('apply_filter')
def handle_filter(data):
    filter_type = data.get('filter_type')
    selected_ingredients = data.get('selected_ingredients')
    recipes = list(db.filter_recipes(filter_type, selected_ingredients))
    sanitized_recipes = mongo_to_json(recipes)
    socketio.emit('update_recipes', sanitized_recipes)

@socketio.on('shutdown_signal')
def handle_shutdown_signal():
    global should_shutdown
    should_shutdown = True

def run_app():
    while not should_shutdown:
        socketio.sleep(1)
    socketio.stop()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)

#if __name__ == '__main__':
#    socketio.run(app)
