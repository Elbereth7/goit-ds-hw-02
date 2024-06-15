from faker import Faker
from random import randint
import sqlite3
import db.queries.insert as insert

def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []# тут зберігатимемо користувачів
    fake_tasks = []# тут зберігатимемо завдання
    
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = Faker()

    # Створимо набір користувачів у кількості number_users
    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_tasks):
        fake_tasks.append((fake_data.catch_phrase(), fake_data.paragraph(nb_sentences=3)))

    return fake_users, fake_tasks

def prepare_data(users, tasks) -> tuple():
    for_users = []
    # Готуємо список кортежів назв компаній
    for user in users:
        for_users.append(user)

    for_tasks = []  # для таблиці employees

    for task in tasks:
        """
        Для записів у таблицю співробітників нам потрібно додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число, збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
        """
        for_tasks.append(task + (randint(1, 3), randint(1, len(for_users))))

    return for_users, for_tasks


def insert_data_to_db(users, tasks) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними

    with sqlite3.connect("tasks.db") as con:

        cur = con.cursor()

        """Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипту, а другим - дані (список кортежів)."""

        cur.executemany(insert.to_users_query, users)

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(insert.to_tasks_query, tasks)

        # Вставляємо дані про зарплати
        statuses = [("new",), ("in progress",), ("completed",)]
        cur.executemany(insert.to_status_query, statuses)

        # Фіксуємо наші зміни в БД

        con.commit()
