# database_module.py

import sqlite3
from datetime import datetime

class DatabaseModule:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                event TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.connection.commit()

    def log_event(self, name, event):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO events (name, event) VALUES (?, ?)
        ''', (name, event))
        self.connection.commit()

    def close(self):
        self.connection.close()
