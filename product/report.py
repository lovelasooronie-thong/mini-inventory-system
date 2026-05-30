import psycopg2
from database.DB import conn, cursor
from auth.login import login



def report_daily_sales(user_id):
    try :

        while True :
            print("select the report : ")
            print("1. id that update product this week")
            print("2. total of update to day")
            print("3. total all product in stock")
            print("4. total stock each of category ")
            print("5. ALL ")
            print("6. exits")

            choice = input("your choice : ")
            if choice == '1':
                id_update_week()

            elif choice == '2':
                update_day()

            elif choice == '3':
                total_stock()
                
            elif choice == '4':
                total_stock_category()
            
                
            elif choice == '5':
                all_report()
            
            elif choice == '6':
                print("Exiting the program.")
                return
            else:
                print("Invalid choice. Please try again.")

    except Exception as e :
        print (e)




def  id_update_week() :
    try:
        print("ตารางจำนวนการเข้าแก้ไขของแต่ละUSER")
        print("[ จำนวน ][ id ][ ชื่อ ]")
        cursor.execute("""
                        SELECT 
                        COUNT(*) ,
                            products.update_by,
                            users.username
                        FROM products
                        INNER JOIN users
                            ON users.id = products.update_by
                        WHERE updated_at >= NOW() - INTERVAL '7 days'
                        GROUP BY products.update_by, users.username
                       """)
        
        rows = cursor.fetchall()
        for row  in rows:
            print(row)
        print("\n\n")

        print("ตารางข้อมูลการแก้ไขล่าสุดและ user ผู้แก้ไข")
        cursor.execute("""
                       select 
                       products.id,
                       products.name,
                       products.stock, 
                       users.username,
                       products.updated_at 
                       from products 
                       inner join users
                        ON users.id = products.update_by 
                       order by products.updated_at DESC
                       limit 5
                       """)
        rows = cursor.fetchall()
        for row  in rows:
            print(row) 
        print("\n\n")   
    except:
        print("Error fetching products")

def  update_day():
    try:
        print("ตารางอัปเดตประจำวัน")
        cursor.execute("""
                        SELECT *
                        FROM products
                        WHERE DATE(products.updated_at) = CURRENT_DATE
                        order BY products.updated_at
                       """)
        
        rows = cursor.fetchall()
        for row  in rows:
            print(row)
        print("\n\n")
    except:
        print("Error fetching products")

def total_stock():
    try:
        print("จำนวนสินค้าทั้งหมดในคลัง")
        cursor.execute("""
                        SELECT SUM(stock) as total
                        FROM products
                       """)
        
        rows = cursor.fetchall()
        for row  in rows:
            print(row)
        print("\n\n")
    except:
        print("Error fetching products")
    
def  total_stock_category():
    try :
        cursor.execute("""
                    SELECT products.category_id,
                        categories.name,
                        SUM(stock) as total
                        FROM products
                    inner join categories
                       ON categories.id = products.category_id
                    where  DATE(products.updated_at) = CURRENT_DATE
                    group by products.category_id,categories.name
                    order by products.category_id ASC
                       """)
        
        rows = cursor.fetchall()
        for row  in rows:
            print(row)
        print("\n\n")
    except:
        print("Error fetching products")

def  all_report() :
    try : 
         id_update_week()
         update_day()
         total_stock()
         total_stock_category()
    
    except:
        print("Error fetching products")






    
    
    





