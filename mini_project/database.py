import sqlite3

def create_tables():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20) UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categories(
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Menu_Items(
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT,
            price INTEGER,
            category_id INTEGER,
            availability TEXT DEFAULT 'Available',
            FOREIGN KEY(category_id) REFERENCES Categories(category_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            item_id INTEGER,
            quantity INTEGER,
            total_price INTEGER,
            payment_method TEXT,
            order_date TEXT,
            FOREIGN KEY(user_id) REFERENCES Users(id),
            FOREIGN KEY(item_id) REFERENCES Menu_Items(item_id)
        )
    """)

    conn.commit()
    conn.close()