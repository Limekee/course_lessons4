from sqlite3 import *
class User():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
def create_table_user(cur):
    command = """CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            gender TEXT); 
                """
    cur.execute(command)
def add_user(cur, user):
    command="""INSERT INTO users(name, surname, gender) VALUES (?, ?, ?);
    """
    cur.execute(command, (user.name, user.surname, user.gender))
def get_user_list(cur):
    command="""
    SELECT * FROM users;
    """
    print(cur.execute(command).fetchall())
def get_user(cur, user_id):
    command="""
    SELECT * FROM users WHERE id = ?;
    """
    print(cur.execute(command, user_id).fetchall())
def update_user_name(cur, name, user_id):
    command="""
    UPDATE users SET name=? WHERE id=?;
    """
    cur.execute(command, (name, user_id))
def delete_users(cur):
    command="""
    DELETE FROM users
    """
    cur.execute(command)
def delete_user(cur, user_id):
    command="""
    DELETE FROM users WHERE id = ?
    """
    cur.execute(command, user_id)
def get_gender_list(cur, gender):
    command="""
    SELECT * FROM users WHERE gender is ?;
    """
    print(cur.execute(command, (gender, )).fetchall())
if __name__=='__main__':
    cur= connect('data.db').cursor()
    create_table_user(cur)
    add_user(cur, User('Mixa', 'Ivanov', 'male'))
    add_user(cur, User('Ekat', 'Ivanova', 'female'))
    add_user(cur, User('Peter', 'Ivanov', 'male'))
    get_user_list(cur)
    connect('data.db').close()

