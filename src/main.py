from db.methods.create_db import create_db
import db.methods.seed as seed


NUMBER_USERS = 5
NUMBER_TASKS = 30


if __name__ == "__main__":
    create_db()
    users, tasks = seed.prepare_data(
        *seed.generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    )
    seed.insert_data_to_db(users, tasks)
