from database import create_tables
from auth import register, login
from admin import admin_menu
from customer import customer_menu

create_tables()

while True:
    print("\n===== Restaurant Menu Management System =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        result = login()

        if result:
            id, role = result

            if role == "admin":
                admin_menu()
            else:
                customer_menu(id)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

