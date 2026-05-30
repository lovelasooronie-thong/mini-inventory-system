import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="store_database",
    user="postgres",
    password="1234" 
)

cursor = conn.cursor()

# การเพิ่มและดูตาราง
# try:
    
# ตรวจสอบการอัพเดตโดยใช้ ID ของผู้ใช้
#     while True: 
#         update_by = int(input("update by ID : "))
#         cursor.execute ("SELECT id from users where id = %s",
#                         (update_by,)
#         )
#         result = cursor.fetchone()
#         if result:
#             break
#         else:
#             print("ีuser ID not found. Please try again.")

#     # การเพิ่มข้อมูลลงตาราง products
#     name = input("Enter product name: ")
#     stock = int(input("Enter product stock: "))
#     category = input ("Enter category : ")

#     cursor.execute(
#         "INSERT INTO products(name,stock,category,update_by) values (%s , %s ,%s ,%s)",
#         (name,stock,category,update_by)
#     )

#     conn.commit()
#     print ("Added successfully")

#     # แสดงข้อมูลจากตาราง products

#     cursor.execute("SELECT * FROM products")

#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)

# except :
#     conn.rollback()

# finally:
#     cursor.close()
#     conn.close()

