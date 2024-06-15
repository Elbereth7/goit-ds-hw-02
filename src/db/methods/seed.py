from faker import Faker
from random import randint
import sqlite3
import db.queries.insert as insert


def generate_fake_data(number_users: int, number_tasks: int) -> tuple():
    """
    Generating fake data for users and tasks tables using Faker
    :param number_users: number of users that we would like to create
    :param number_tasks: number of tasks that we would like to create
    :return: tuple of lists (fake users list and fake tasks list)
    """
    fake_users = []
    fake_tasks = []

    fake_data = Faker()

    # Generate number_users fake users tuples and add them to the list
    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    # Generate number_tasks fake tasks tuples and add them to the list
    for _ in range(number_tasks):
        fake_tasks.append(
            (fake_data.catch_phrase(), fake_data.paragraph(nb_sentences=3))
        )

    return fake_users, fake_tasks


def prepare_data(users, tasks) -> tuple():
    """
    Generating fake data for users and tasks tables using Faker
    :param users: users list
    :param tasks: tasks list
    :return: tuple of lists (data to be inserted to the DB users table and and data to be inserted to the DB tasks table)
    """
    for_users = []
    for user in users:
        for_users.append(user)

    for_tasks = []

    for task in tasks:
        """
        For field status_id in tasks table we are choosing random number in range (1, 3) which is corresponding 
        to one of the possible status values (new, in progress, completed).
        For field user_id in tasks table we are choosing  in range (1, qty of users).
        Adding these fields values to the tuple of generated fake data.
        """
        for_tasks.append(task + (randint(1, 3), randint(1, len(for_users))))

    return for_users, for_tasks


def insert_data_to_db(users, tasks) -> None:

    # Create DB connection and cursor object
    with sqlite3.connect("tasks.db") as con:

        cur = con.cursor()

        """
        Inserting all users' data to DB users table
        :insert.to_users_query: SQL query
        :users: list of tuples with users' data
        """
        cur.executemany(insert.to_users_query, users)

        """
        Inserting all tasks' data to DB tasks table
        :insert.to_tasks_query: SQL query
        :tasks: list of tuples with tasks' data
        """
        cur.executemany(insert.to_tasks_query, tasks)

        statuses = [("new",), ("in progress",), ("completed",)]

        """
        Inserting all statuses' data to DB status table
        :insert.to_status_query: SQL query
        :statuses: list of tuples with statuses' data
        """
        cur.executemany(insert.to_status_query, statuses)

        # Commit the DB changes
        con.commit()
