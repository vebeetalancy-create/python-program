import sqlite3
import re

def register():
    print("\n===== REGISTER USER =====")

    username = input("Enter username: ").strip()

    if len(username) > 20:
        print("Username should not exceed 20 characters.")
        return

    password = input("Enter password: ")

    # Password validations
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return

    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return

    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return

    if not re.search(r"[0-9]", password):
        print("Password must contain at least one number.")
        return

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must contain at least one special character.")
        return

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, password, "customer"))

        conn.commit()
        print("Registered successfully!")

    except sqlite3.IntegrityError:
        print("Username already exists. Please choose another username.")
    
    finally:
        if conn:
            conn.close()

    

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, role
            FROM Users
            WHERE username=? AND password=?
        """, (username, password))

        user = cursor.fetchone()

        if user:
            print("Login Successful!")
            return user
        else:
            print("Invalid Username or Password!")
            return None

    finally:
        if conn:
            conn.close()
    