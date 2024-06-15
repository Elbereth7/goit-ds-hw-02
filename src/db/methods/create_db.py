import sqlite3


def create_db():
    # Read the file with SQL script
    with open("src/db/scripts/tasks.sql", "r") as f:
        sql = f.read()

    # Create connection with DB and execute script to create tables
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        cur.executescript(sql)
