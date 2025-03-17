from init_db import get_db_connection

def create_todo(title,description,status):
    db = get_db_connection()
    db.execute("INSERT INTO todos (title, description,status) VALUES (?, ?, ?)",(title,description,status))
    db.commit()
    db.close()

def get_todos():
    db = get_db_connection()
    cursor = db.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    db.close()
    return todos

def update_todo(id,title,description,status):
    db = get_db_connection()
    db.execute("UPDATE todos SET title = ?,description = ?, status = ? WHERE id = ?",(title,description,status,id))
    db.commit()
    db.close()

def delete_todo(id):
    db = get_db_connection()
    db.execute("DELETE FROM todos WHERE id = ?", (id,))
    db.commit()
    db.close()

def find_todo(id):
    db = get_db_connection()
    cursor = db.execute("SELECT * FROM todos WHERE id = ?", (id,))
    todo = cursor.fetchone()
    db.close()
    return todo
