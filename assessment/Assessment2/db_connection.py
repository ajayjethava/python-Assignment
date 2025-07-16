import pymysql
# from hotel_db import *

class DatabaseConnection:
    def __init__(self):
        try:
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="hotel_management"
            )
            self.cursor = self.db.cursor()
        except Exception as e:
            print("Database Connection Failed:", e)

    def execute(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            return self.cursor
        except Exception as e:
            print("Database Error:", e)
            return None

    def close(self):
        self.cursor.close()
        self.db.close()
