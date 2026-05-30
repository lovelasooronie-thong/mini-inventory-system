import psycopg2
from database.DB import conn, cursor
from auth.login import login
   
# cursor.execute()= ส่ง SQL ไปหา PostgreSQL
# fetchone()ใช้ดึง “1 แถว
# fetchall()ใช้ดึง “ทุกแถว”

def add_product(user_id):
    try:

        # การเพิ่มข้อมูลลงตาราง products
        update_by = int(user_id)
        name = input("Enter product name: ")
        stock = int(input("Enter product stock: "))
        category = input ("Enter category_id : ")

        cursor.execute(
            "INSERT INTO products(name,stock,category_id,update_by) values (%s , %s ,%s ,%s)",
            (name,stock,category,update_by)
        )

        conn.commit()
        print ("Added successfully")


    except :
        conn.rollback()

    

def view_products(user_id):
    try:
        cursor.execute("select * from products order by id ")
        rows = cursor.fetchall()
        for row  in rows:
            print(row)
    except:
        print("Error fetching products")
   

def delete_product(user_id):
    try:
        cursor.execute("select * from products order by id ")
        rows = cursor.fetchall()
        for row  in rows:
            print(row)

        product_id = int(input("Enter product ID to delete: "))
        wranning = input("!!!Are you sure you want to delete this product? (yes/no): ")

        if wranning.lower() == "yes":
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        else: 
             print("Deletion cancelled.")
        conn.commit()
        print("Product deleted successfully")

    except:
        conn.rollback()
        print("Error occurred while deleting product.")

def update_stock(user_id):

    try:

        cursor.execute("SELECT * FROM products ORDER BY id")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        id_update = int(input("ID which you want to update : "))

        cursor.execute(
            "SELECT * FROM products WHERE id = %s",
            (id_update,)
        )

        stock_data = cursor.fetchone()

        if not stock_data:
            print("Product not found")
            return

        stock = stock_data[2]

        print("Select your choice")
        print("1. Add stock")
        print("2. Delete stock")
        print("3. New stock")

        choice = input("Your choice : ")

        if choice == '1':
            add_stock(stock, id_update)

        elif choice == '2':
            delete_stock(stock, id_update)
        elif choice == '3':
            new_stock(id_update)

        else:
            print("Try again")
            return

        conn.commit()

        print("Product updated successfully")

    except Exception as e:

        conn.rollback()
        print(e)
    
def add_stock(stock,id_update):
    now = stock 
    id = id_update
    cal = int(input("count of add : "))
    new = now + cal 
    cursor.execute ("update products set stock = %s  updated_at = CURRENT_TIMESTAMP  where id = %s",
                        (new,id)
    )

def delete_stock(stock,id_update):
    now = stock 
    id = id_update
    cal = int(input("count of add : "))
    new = now - cal 
    if new < 0 :
        print("stock can't < 0")
    else :
        cursor.execute ("update products set stock = %s  updated_at = CURRENT_TIMESTAMP where id = %s",
                        (new,id)
    )
        
def new_stock(id_update):
    id = id_update
    new =(int(input("enter new stock : ")))
    cursor.execute ("update products set stock = %s  updated_at = CURRENT_TIMESTAMP where id = %s",
                        (new,id)
    )



def search_products(user_id):
    try:
        search_word =input(" search products name : ")
        word = search_word.lower()
        cursor.execute("SELECT * FROM products where name Ilike %s", (f"%{word}%",))
        result_search = cursor.fetchall()
        if not result_search:
            print ("Product not found")
            return
        for row in  result_search :
                print(row)

       
    except:
      print("Error fetching products")


     


 


