"""Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, помітимо
знаком заповнювача (?) """

to_users_query = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""
                               
# Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

to_tasks_query = """INSERT INTO tasks(title, description, status_id, user_id)
                        VALUES (?, ?, ?, ?)"""
                               
# Останньою заповнюємо таблицю із зарплатами

to_status_query = """INSERT INTO status(name)
                        VALUES (?)"""
