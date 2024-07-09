from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

app = Flask(__name__)

init_app(app)

CORS(app)

app.route('/', methods=['GET'])(index)
app.route('/tabla/crear/', methods=['POST'])(crear_tabla)
app.route('/api/games/', methods=['GET'])(get_all_games)
app.route('/api/games/<int:game_id>', methods=['GET'])(get_game)
app.route('/api/games/<int:game_id>', methods=['PUT'])(update_game)
app.route('/api/games/<int:game_id>', methods=['DELETE'])(delete_game)

if __name__ == '__main__':
    app.run(debug=True)