# Insert user's data to DB users table
to_users_query = """INSERT INTO users(fullname, email)
                    VALUES (?, ?)"""

# Insert task's data to DB tasks table
to_tasks_query = """INSERT INTO tasks(title, description, status_id, user_id)
                    VALUES (?, ?, ?, ?)"""

# Insert status's data to DB status table
to_status_query = """INSERT INTO status(name)
                    VALUES (?)"""

# Add new task for a specific user id
new_task_for_user_query = """INSERT INTO tasks(title, description, status_id, user_id)
                            VALUES (?, ?, 1, ?)"""
