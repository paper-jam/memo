import sqlite3

conn = sqlite3.connect("C:newhello.db")  # create file if doses not exist
curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY,name TEXT NOT NULL,priority INTEGER NOT NULL);""")


# -- delete all data
curs.execute("DELETE FROM tasks ")
conn.commit()


tasks = [
    (1, "My first task", 1),
    (2, "My second task", 5),
    (3, "My third task", 10),
]
curs.executemany("INSERT INTO tasks (id, name, priority) VALUES (?,?,?)", tasks)
conn.commit()

# --- verify data
for row in curs.execute("SELECT * FROM tasks"):
    print(row)

print("*" * 30)

# -- many update

new_prio = [
    (10, 1),
    (100, 2),
    (1000, 3),
]

curs.executemany("UPDATE tasks SET priority = ? WHERE id = ?", new_prio)

conn.commit()

# --- verify data
for row in curs.execute("SELECT * FROM tasks"):
    print(row)


conn.commit()
conn.close()
