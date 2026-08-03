import sqlite3

def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Update Menu Item")
        print("4. Delete Menu Item")
        print("5. Manage Categories")
        print("6. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            add_menu_item()
        elif ch == "2":
            view_menu()
        elif ch == "3":
            update_menu_item()
        elif ch == "4":
            delete_menu_item()
        elif ch == "5":
            manage_categories()
        elif ch == "6":
            break


def add_menu_item():

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        view_categories()

        category_id = int(input("Enter Category ID: "))
        item_name = input("Enter Item Name: ").strip()
        price = int(input("Enter Price: "))

        cursor.execute("""
            INSERT INTO Menu_Items(item_name, price, category_id)
            VALUES (?, ?, ?)
        """, (item_name, price, category_id))

        conn.commit()
        print("Menu Item Added Successfully ✅")

    except ValueError:
        print("Category ID and Price must be numbers.")

    except sqlite3.IntegrityError:
        print("Invalid Category ID or duplicate data.")

    finally:
        if conn:
            conn.close()


def view_menu():

    conn = None
    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                item_id,
                item_name,
                category_name,
                price,
                availability
            FROM Menu_Items
            JOIN Categories
            ON Menu_Items.category_id = Categories.category_id
        """)

        menu = cursor.fetchall()

        print("\n=========== MENU ===========")

        print("{:<5} {:<20} {:<15} {:<10} {:<12}".format(
            "ID", "Item", "Category", "Price", "Status"
        ))

        print("-" * 65)

        if menu:
            for row in menu:
                print("{:<5} {:<20} {:<15} {:<10} {:<12}".format(*row))
        else:
            print("No menu items found.")

    finally:
        if conn:
            conn.close()



def update_menu_item():

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        view_menu()

        item_id = int(input("Enter Item ID to update: "))

        item_name = input("New Item Name: ").strip()
        price = int(input("New Price: "))
        availability = input("Availability (Available/Unavailable): ").strip()

        view_categories()
        category_id = int(input("New Category ID: "))

        cursor.execute("""
            UPDATE Menu_Items
            SET
                item_name=?,
                price=?,
                category_id=?,
                availability=?
            WHERE item_id=?
        """, (item_name, price, category_id, availability, item_id))

        if cursor.rowcount == 0:
            print("No menu item found with that ID.")
        else:
            conn.commit()
            print("Menu Updated Successfully ✅")

    except ValueError:
        print("Item ID, Category ID, and Price must be numbers.")

    except sqlite3.IntegrityError:
        print("Invalid Category ID.")
    
    finally:
        if conn:
            conn.close()


def delete_menu_item():

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        view_menu()

        item_id = int(input("Enter Item ID to delete: "))

        cursor.execute("""
            DELETE FROM Menu_Items
            WHERE item_id = ?
        """, (item_id,))

        if cursor.rowcount == 0:
            print("No menu item found with that ID.")
        else:
            conn.commit()
            print("Item Deleted Successfully ✅")

    except ValueError:
        print("Item ID must be a number.")

    finally:
        if conn:
            conn.close()

def manage_categories():

    while True:

        print("\n===== CATEGORY MENU =====")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Delete Category")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_category()

        elif choice == "2":
            view_categories()

        elif choice == "3":
            delete_category()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")



def add_category():

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        category_name = input("Enter Category Name: ").strip()

        if category_name == "":
            print("Category name cannot be empty.")
            return

        # Check if category already exists
        cursor.execute("""
            SELECT *
            FROM Categories
            WHERE category_name = ?
        """, (category_name,))

        if cursor.fetchone():
            print("Category already exists.")
        else:
            cursor.execute("""
                INSERT INTO Categories(category_name)
                VALUES(?)
            """, (category_name,))

            conn.commit()
            print("Category Added Successfully ✅")

    except sqlite3.IntegrityError:
        print("Category already exists.")
    
    finally:
        if conn:
            conn.close()


def view_categories():

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Categories")

        categories = cursor.fetchall()

        print("\n===== Categories =====")

        if categories:
            for category in categories:
                print(f"{category[0]}. {category[1]}")
        else:
            print("No categories found.")
    
    finally:
        if conn:
            conn.close()



def delete_category():

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        # Display all categories
        cursor.execute("""
            SELECT * FROM Categories
        """)

        categories = cursor.fetchall()

        if not categories:
            print("No Categories Found.")
            return

        print("\n===== CATEGORY LIST =====")

        for category in categories:
            print(f"{category[0]}. {category[1]}")

        category_id = int(input("\nEnter Category ID to Delete: "))

        # Check whether category exists
        cursor.execute("""
            SELECT * FROM Categories
            WHERE category_id = ?
        """, (category_id,))

        if cursor.fetchone() is None:
            print("Invalid Category ID.")
            return

        # Check whether any menu item uses this category
        cursor.execute("""
            SELECT * FROM Menu_Items
            WHERE category_id = ?
        """, (category_id,))

        if cursor.fetchone():
            print("Cannot delete category.")
            print("This category contains menu items.")
            return

        cursor.execute("""
            DELETE FROM Categories
            WHERE category_id = ?
        """, (category_id,))

        conn.commit()
        print("Category Deleted Successfully ✅")

    except ValueError:
        print("Category ID must be a number.")

    finally:
        if conn:
            conn.close()