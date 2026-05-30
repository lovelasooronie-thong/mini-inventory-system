import psycopg2
from database.DB import conn, cursor

def login():
    while True: 
            username = (input("Username : : "))
            password = (input("password : "))
            cursor.execute ("SELECT id from users where username = %s and password = %s",
                            (username, password,)
            )
            result = cursor.fetchone()
            if result:
                    update_by = result[0]
                    print("Login successful")
                    return update_by
            else:
                print("Invalid username or password")