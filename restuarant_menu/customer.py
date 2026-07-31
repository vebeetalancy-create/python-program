import sqlite3
from datetime import datetime


def customer_menu(user_id):
    while True:
        print("\n===== CUSTOMER MENU =====")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Order History")
        print("4. Bill")
        print("5. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            view_menu()

        elif ch == "2":
            place_order(user_id)

        elif ch == "3":
            order_history(user_id)

        elif ch == "4":
            bill(user_id)

        elif ch == "5":
            print("Logged Out Successfully.")
            break

        else:
            print("Invalid Choice!")

def view_menu():
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
        WHERE availability='Available'
    """)

    menu = cursor.fetchall()

    if not menu:
        print("No Menu Items Available.")
        conn.close()
        return

    print("\n========== MENU ==========")
    print("{:<5}{:<20}{:<15}{:<10}".format(
        "ID","Item","Category","Price"
    ))
    print("-"*55)

    for row in menu:
        print("{:<5}{:<20}{:<15}{:<10}".format(
            row[0],row[1],row[2],row[3]
        ))

    conn.close()



# def place_order(user_id):

#     conn = None

#     try:
#         view_menu()

#         item_id = int(input("\nEnter Item ID: "))
#         quantity = int(input("Enter Quantity: "))

#         if quantity <= 0:
#             print("Quantity must be greater than 0.")
#             return

#         conn = sqlite3.connect("restaurant.db")
#         cursor = conn.cursor()

#         cursor.execute("""
#             SELECT price
#             FROM Menu_Items
#             WHERE item_id = ? AND availability = 'Available'
#         """, (item_id,))

#         item = cursor.fetchone()

#         if item is None:
#             print("Invalid Item.")
#             return

#         price = item[0]
#         total_price = price * quantity

#         payment = input("Payment Method (Cash/UPI/Card): ").strip()

#         if payment not in ["Cash", "UPI", "Card"]:
#             print("Invalid Payment Method.")
#             return

#         order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         cursor.execute("""
#             INSERT INTO Orders(
#                 user_id,
#                 item_id,
#                 quantity,
#                 total_price,
#                 payment_method,
#                 order_date
#             )
#             VALUES (?, ?, ?, ?, ?, ?)
#         """, (user_id, item_id, quantity, total_price, payment, order_date))

#         conn.commit()
#         print("Order Placed Successfully ✅")

#     except ValueError:
#         print("Item ID and Quantity must be numbers.")
    
#     finally:
#         if conn:
#             conn.close()



def place_order(user_id):

    conn = None

    try:
        conn = sqlite3.connect("restaurant.db")
        cursor = conn.cursor()

        ordered_items = set()   # Stores already selected item_ids

        while True:

            view_menu()

            try:
                item_id = int(input("\nEnter Item ID: "))

                if item_id in ordered_items:
                    print("This item is already added. Choose another menu item.")
                    continue

                quantity = int(input("Enter Quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

            except ValueError:
                print("Item ID and Quantity must be numbers.")
                continue

            cursor.execute("""
                SELECT price
                FROM Menu_Items
                WHERE item_id=? AND availability='Available'
            """, (item_id,))

            item = cursor.fetchone()

            if item is None:
                print("Invalid Item.")
                continue

            price = item[0]
            total_price = price * quantity

            payment = input("Payment Method (Cash/UPI/Card): ").strip()

            if payment not in ["Cash", "UPI", "Card"]:
                print("Invalid Payment Method.")
                continue

            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                INSERT INTO Orders(
                    user_id,
                    item_id,
                    quantity,
                    total_price,
                    payment_method,
                    order_date
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, item_id, quantity, total_price, payment, order_date))

            conn.commit()

            ordered_items.add(item_id)

            print("Item Added Successfully ✅")

            choice = input("\nAdd another item? (Y/N): ").strip().lower()

            if choice != "y":
                print("Order Completed Successfully ✅")
                break

    finally:
        if conn:
            conn.close()

def order_history(user_id):

    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            Orders.order_id,
            Menu_Items.item_name,
            Orders.quantity,
            Orders.total_price,
            Orders.payment_method,
            Orders.order_date
        FROM Orders
        JOIN Menu_Items
        ON Orders.item_id=Menu_Items.item_id
        WHERE Orders.user_id=?
    """,(user_id,))

    orders = cursor.fetchall()

    if not orders:
        print("No Orders Found.")
        conn.close()
        return

    print("\n========== ORDER HISTORY ==========")

    print("{:<5}{:<20}{:<10}{:<10}{:<12}{}".format(
        "ID","Item","Qty","Total","Payment","Date"
    ))

    print("-"*80)

    for row in orders:
        print("{:<5}{:<20}{:<10}{:<10}{:<12}{}".format(*row))

    conn.close()



def bill(user_id):

    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            Menu_Items.item_name,
            Orders.quantity,
            Orders.total_price,
            Orders.payment_method,
            Orders.order_date
        FROM Orders
        JOIN Menu_Items
        ON Orders.item_id = Menu_Items.item_id
        WHERE Orders.user_id = ?
        ORDER BY Orders.order_id DESC
    """, (user_id,))

    bills = cursor.fetchall()

    if not bills:
        print("No Orders Found.")
        conn.close()
        return

    print("\n============= BILL =============")
    print(f"{'Item':15}{'Qty':>5}{'Price':>10}")

    grand_total = 0

    for bill in bills:
        print(f"{bill[0]:15}{bill[1]:>5}{bill[2]:>10.2f}")
        grand_total += bill[2]

    print("-" * 32)
    print(f"{'Grand Total':20}{grand_total:>10.2f}")

    print(f"\nPayment Method : {bills[0][3]}")
    print(f"Order Date     : {bills[0][4]}")

    print("\nThank You! Visit Again 😊")

    conn.close()