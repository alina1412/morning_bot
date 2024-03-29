"""classes Data and Collector to keep track of user choices
in sqlite db"""
import sqlite3


class Data:
    def __init__(self) -> None:
        self.db = "choices.db"
        self.table_name = "users"
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db)
        except sqlite3.Error as error:
            print(error)

    def create(self):
        query = f"""CREATE table IF NOT EXISTS
            {self.table_name} (user_id INTEGER PRIMARY KEY,
            choice TEXT NOT NULL)"""
        with self.conn:
            self.conn.execute(query)
            self.conn.commit()

    def update_decision(self, user_id, choice):
        query = f"""UPDATE {self.table_name}
            SET choice = '{choice}'
            WHERE user_id = {user_id}"""
        with self.conn:
            self.conn.execute(query)
            self.conn.commit()

    def select_sql(self, condition=""):
        query = f"SELECT * FROM {self.table_name}" + " " + condition
        with self.conn:
            return self.conn.execute(query)

    def insert(self, user_id, choice):
        query = f"""INSERT into {self.table_name}
            (user_id, choice)
            VALUES (?,?)"""
        with self.conn:
            self.conn.execute(query, (user_id, choice))
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()


class Collector:
    def __init__(self) -> None:
        self.db = Data()
        self.db.connect()
        self.db.create()

    def save_choice(self, user_id, choice):
        try:
            self.db.insert(user_id, choice)
        except Exception:
            self.db.update_decision(user_id, choice)

    def get_choice(self, user_id):
        condition = f"WHERE user_id = {user_id}"
        pair = list(self.db.select_sql(condition))
        return pair[0][1] if pair else []

    def get_all_choices(self):
        return list(self.db.select_sql())
