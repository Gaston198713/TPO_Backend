from flask import jsonify, request
from app.models import Game
from app.database import *

def index():
    return jsonify({'message': 'La API de juegos esta conectada'})

def create_game():
    data = request.json
    new_game = Game(title=data['title'], genero=data['genero'], banner=data['banner'])
    new_game.save()
    return jsonify({'message': 'Game created successfully'}), 201

def get_all_games():
    games = Game.get_all()
    return jsonify([games.serialize() for game in games])

def get_game(game_id):
    game = Game.get_by_id(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404
    return jsonify(game.serialize())

def update_game(game_id):
    game = Game.get_by_id(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404
    data = request.json
    game.banner = data['banner']
    game.save()
    game.title = data['title']
    return jsonify({'message': 'Game updated successfully'})
    

def delete_game(game_id):
    game = Game.get_by_id(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404
    game.delete()
    return jsonify({'message': 'Game deleted successfully'})

def crear_tabla():
    try:
        crear_tabla_juegos()
        return jsonify({"mensaje":"Ya se creo la tabla o ya existia"}),200
    except BaseException as be:
        return jsonify({"mensaje":"hasta las manos"}),500
