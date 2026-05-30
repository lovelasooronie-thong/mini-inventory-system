
from auth.login import login
import product.product as product
import product.report as report
from database.DB import conn, cursor

while True:
    user_id = login()
    if user_id:
        print(f"Welcome what do you want to do? ")
        break
    else:
        print("Login failed. Please try again.")


while True:
    print("1.Add product")
    print("2.View products")
    print("3.Update stock")
    print("4.Delete product")
    print("5.Search products")
    print("6.Report on daily sales")
    print("7.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        product.add_product(user_id)
    elif choice == '2':
        product.view_products(user_id)
    elif choice == '3':
        product.update_stock(user_id)
    elif choice == '4':
        product.delete_product(user_id)
    elif choice == '5':
        product.search_products(user_id)
    elif choice == '6':
        report.report_daily_sales(user_id)
    elif choice == '7':
        print("Exiting the program.")
        cursor.close()
        conn.close()
        break
    else:
        print("Invalid choice. Please try again.")

    print()  # blank line for readability