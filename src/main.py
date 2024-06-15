from db.methods.create_db import create_db
import db.methods.seed as seed
import db.methods.execute_queries as execute
import db.queries.select as select
import db.queries.insert as insert
import db.queries.update as update
import db.queries.delete as delete

NUMBER_USERS = 8
NUMBER_TASKS = 30


def show_query_result(query, *args):
    if query.startswith("SELECT"):
        print(
            f"""Result of query '{query}' with parameters {args}:\n
{execute.fetch_data(query, *args)}\n
{'-'*40}"""
        )
    else:
        print(f"It's not a SELECT query\n{'-'*40}")


if __name__ == "__main__":
    create_db()
    users, tasks = seed.prepare_data(
        *seed.generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    )
    seed.insert_data_to_db(users, tasks)

    show_query_result(select.tasks_by_userid_query, 1)
    show_query_result(select.tasks_by_statusname_query, "new")
    show_query_result(select.users_no_tasks_query)
    show_query_result(select.tasks_not_completed_query)
    show_query_result(select.users_by_email_query, "@example.net")
    show_query_result(select.tasks_qty_by_status_query)
    show_query_result(select.tasks_by_user_domain_query, "example.com")
    show_query_result(select.users_tasks_by_status_name_query, "in progress")
    show_query_result(select.users_tasks_qty_query)

    execute.change_data(
        insert.new_task_for_user_query, "Read the instructions", None, 7
    )
    execute.change_data(insert.new_task_for_user_query, "Wash the car", None, 1)
    show_query_result(select.tasks_no_descr_query)

    execute.change_data(update.task_status_query, "in progress", 32)
    execute.change_data(update.user_name_query, "Nataliya Yakovenko", 7)
    execute.change_data(delete.task_by_id_query, 33)

    execute.change_data(update.user_email_query, "harrynielsen@example.com", 2)
    execute.change_data(update.status_name_query, "new", 2)
    execute.change_data(delete.user_by_id_query, 1)
