import mysql.connector as cobj

config = {
    "host": "localhost",
    "username": "root",
    "database": "py_db1",
    "password": ""
}

conn = cobj.connect(**config).is_connected()
print(conn)
# print(conn.is_connected())