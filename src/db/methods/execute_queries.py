import sqlite3


def fetch_data(sql: str, *args) -> list:
    """
    Execute SELECT queries to get data from DB
    :param sql: query string
    :param args: all the arguments required for the specific query
    :return: list of tuples
    """
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        cur.execute(sql, args)
        return cur.fetchall()


def change_data(sql: str, *args):
    """
    Execute UPDATE, INSERT and DELETE queries to modify data in the DB
    :param sql: query string
    :param args: all the arguments required for the specific query
    :return: None
    """
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        try:
            cur.execute(
                "PRAGMA foreign_keys = ON;"
            )  # Ensure that foreign key constraints are enabled
            cur.execute(sql, args)
            con.commit()
        except sqlite3.Error as e:
            print(e)
