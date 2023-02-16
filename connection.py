import mysql.connector

# Connect with mysql db using Python
try:
    conn = mysql.connector.connect(database="py_db1", user="root", password="", host="localhost")
    if conn.is_connected():
        print("DB Connected")
except:
    print("couldn't be connect")

# if conn.is_connected():
#     print("DB Connected")
# else:
#     print("couldn't be connect")

# close connection
print(conn.is_closed())
conn.close()

print(conn.is_closed())