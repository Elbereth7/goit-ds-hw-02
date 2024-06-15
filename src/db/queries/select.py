# Get all tasks for a user id
tasks_by_userid_query = """SELECT id, title, description 
                        FROM tasks 
                        WHERE user_id = ?"""

# Get all tasks with a particular status name (eg. 'new')
tasks_by_statusname_query = """SELECT id, title, description 
                            FROM tasks
                            WHERE status_id = (SELECT id FROM status WHERE name = ?)"""

# Get users with no task assigned using subquery
users_no_tasks_query = """SELECT * 
                        FROM users
                        WHERE id NOT IN (SELECT user_id FROM tasks)"""

# Get all tasks which are not completed
tasks_not_completed_query = """SELECT id, title, description 
                        FROM tasks
                        WHERE status_id != (SELECT id FROM status WHERE name = 'completed')"""

# Filter users by email fragment
users_by_email_query = """SELECT *
                        FROM users
                        WHERE email LIKE '%' || ? || '%'"""

# Get number of tasks for each of the statuses
tasks_qty_by_status_query = """SELECT status.name, COUNT(*)
                            FROM tasks 
                            LEFT JOIN status ON tasks.status_id = status.id
                            GROUP BY status.id"""

# Get tasks for users with specified domain (eg.'%@example.com')
tasks_by_user_domain_query = """SELECT t.id, t.title, t.description
                                FROM tasks as t
                                LEFT JOIN users as u ON t.user_id = u.id
                                WHERE u.email LIKE '%' || ?"""

# Get tasks with missing description
tasks_no_descr_query = """SELECT id, title, description
                    FROM tasks 
                    WHERE description ISNULL"""

# Get users and tasks with a specified status name
users_tasks_by_status_name_query = """SELECT t.user_id, u.fullname, u.email, t.id as task_id, t.title, t.description FROM users as u
                                    INNER JOIN tasks as t ON u.id = t.user_id
                                    WHERE status_id = (SELECT id FROM status WHERE name = ?)
                                    ORDER BY user_id"""

# Get user names with number of corresponding tasks
users_tasks_qty_query = """SELECT u.fullname, COUNT(*) FROM tasks as t
                        LEFT JOIN users as u ON t.user_id = u.id
                        GROUP BY t.user_id"""
