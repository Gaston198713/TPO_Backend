import os
import psycopg2
from flask import g
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 2367)  # puerto predeterminado es 3306 si no se especifica
}

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    

def crear_tabla_juegos():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Juegos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50)  NOT NULL,
            genero VARCHAR(300) NOT NULL,
            completada BOOLEAN NOT NULL,
            activo BOOLEAN NOT NULL
        );
        """
        )
    conn.commit()
    cur.close()
    conn.close()