from app.database import get_db

class Game:
    def __init__(self, id_game=None, title=None, genero=None, banner=None):
        self.id_game = id_game
        self.title = title
        self.genero = genero
        self.banner = banner

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_game:
            cursor.execute("""
                UPDATE games SET title = %s, genero = %s, banner = %s
                WHERE id_game = %s
            """, (self.title, self.genero, self.banner, self.id_game))
        else:
            cursor.execute("""
                INSERT INTO games (title, genero, banner) VALUES (%s, %s, %s, %s)
            """, (self.title, self.banner))
            self.id_game = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM games")
        rows = cursor.fetchall()
        games = []
        for row in rows:
            games.append(Game(id_game=row[0], title=row[1], genero=[2], banner=row[3]))

        
        cursor.close()
        return games

    @staticmethod
    def get_by_id(game_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM games WHERE id_game = %s", (game_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Game(id_game=row[0], title=row[1], genero=row[2], banner=row[3])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM games WHERE id_game = %s", (self.id_game,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_game': self.id_game,
            'title': self.title,
            'diector': self.genero,
            'banner': self.banner
        }