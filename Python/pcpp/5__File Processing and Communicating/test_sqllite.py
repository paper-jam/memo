import sys
import sqlite3

conn = sqlite3.connect("tasks.db")  # create file if doses not exist

# creating table
c = conn.cursor()
c.execute("""CREATE TABLE tasks (id INTEGER PRIMARY KEY,name TEXT NOT NULL,priority INTEGER NOT NULL);""")
conn.commit()

def show_task():
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    res = cur.fetchall()
    if res:
        print(" ---------------------------- ")
        for row in res:
            print(row)
        print(" ---------------------------- ")
    else:
        print("-------- no task in the list ----------")

    cur.close()


def add_task(name, priority):
    conn.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", (name, priority))
    conn.commit()


def change_priority(id_task, new_priority):
    conn.execute("UPDATE tasks SET priority = ? WHERE id = ?", (new_priority, id_task))
    conn.commit()
    

def delete_task(id_task):
    conn.execute("DELETE FROM tasks WHERE id = ?", (id_task,))
    conn.commit()


while True:
    print(" ---------------------------- ")
    print("1. Show Tasks ")
    print("2. Add Task ")
    print("3. Change Priority ")
    print("4. Delete Task")
    print("5. Exit")

    x = int(input("Votre choix ?"))

    if x not in range(1, 6):
        conn.close()
        sys.exit(-1)

    show_task()

    match x:
        case 1:
            show_task()
        case 2:
            lib, priority = input("libelle et priorité de la tâche : ").split()
            add_task(lib, priority)
        case 3:
            id_task, new_priority = input("id tâche et nouvelle priorité : ").split()
            change_priority(id_task, new_priority)
        case 4:
            id_task = input("id tâche à supprimer :")
            delete_task(id_task)
        case 5:
            conn.close()
            sys.exit()
