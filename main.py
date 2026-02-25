import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")
conn.commit()


def add_user():
    name = input("Name: ")
    age = int(input("Age: "))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("User added!")


def show_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def delete_user():
    user_id = int(input("User ID: "))
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    print("Deleted!")


while True:
    print("\n1.Add 2.Show 3.Delete 0.Exit")
    choice = input("> ")

    if choice == "1":
        add_user()
    elif choice == "2":
        show_users()
    elif choice == "3":
        delete_user()
    else:
        break

conn.close()
