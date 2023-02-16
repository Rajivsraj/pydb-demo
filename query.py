import mysql.connector

try:
    conn = mysql.connector.connect(database="py_db1", user="root", password="", host="localhost")
    # if conn.is_connected():
    #     print("DB Connected")
except:
    print("couldn't be connect")


# Show all database
# cur_obj = conn.cursor()
# cur_obj.execute("show databases")
# for db in cur_obj:
#     print(db)


# ==========================
# Create Table in db
# ==========================
# qry = "create table student(roll int primary key auto_increment, name varchar(20), city varchar(20), dept varchar(20))"
# cur_obj = conn.cursor()
# cur_obj.execute(qry)
# print(cur_obj)


# ==========================
# insert data into Table
# ==========================
# qry = "insert into student(name, city, dept) values('Saurav', 'Delhi', 'Marketing'), ('Mohan Pyare', 'Punjab', 'IT')"
# cur_obj = conn.cursor()
# cur_obj.execute(qry)
# print(cur_obj)


# ==========================
# insert data into Table
# ==========================
try:
    qry = "insert into student(name, city, dept) values('Saurav', 'Delhi', 'Marketing'), ('Mohan Pyare', 'Punjab', 'IT')"
    cur_obj = conn.cursor()
    cur_obj.execute(qry)
    conn.commit()
    print("Data Inserted")
except:
    conn.rollback()
    print("Couldn't be add data")