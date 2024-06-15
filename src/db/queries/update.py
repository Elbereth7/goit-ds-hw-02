# Update task's status
task_status_query = """UPDATE tasks
                    SET status_id = (SELECT id FROM status WHERE name = ?)
                    WHERE id = ?"""

# Update user's fullname
user_name_query = """UPDATE users
                    SET fullname = ?
                    WHERE id = ?"""

# Update user's email
user_email_query = """UPDATE users
                    SET email = ?
                    WHERE id = ?"""

# Update status name
status_name_query = """UPDATE status
                    SET name = ?
                    WHERE id = ?"""
