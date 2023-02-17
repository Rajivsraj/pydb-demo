import mysql.connector as mysql

# check connection
# ====================
try:
    conn = mysql.connect(username="root", password="", host="localhost", database="pydb")
    # print("connected")
except:
    print("can't connect")


# CREATE DATABASE USING PYTHON
# =================================
# my_cur = conn.cursor()
# my_cur.execute("create database py_db2")


# CREATE TABLE
# my_cur = conn.cursor()
# my_cur.execute("create table student(rollno int primary key auto_increment, name varchar(30), city varchar(30))")
# print(my_cur)



# # SHOW TABLES OF DB
# # ========================
# my_cur = conn.cursor()
# my_cur.execute("show tables")
#
# # print all the tables using loop
# for table in my_cur:
#     print(table)


# # CRUD: Create, Read, Update, Delete
# ===========================================

# INSERT DATA INTO TABLE
# ========================
"""
my_cur = conn.cursor()

# insert single data/row at once
# my_cur.execute("insert into student(name, city) values('Mohan Pyare', 'delhi')")
# print(my_cur.lastrowid)   # it will give the latest record pk id

# Insert multiple values/data/rows at once
my_cur.execute("insert into student(name, city) values('Rahul', 'delhi'), ('Ankit', 'delhi'), ('Abhishedk', 'delhi'), ('Aman', 'Mumbai')")
# print(my_cur.lastrowid)
print(my_cur.rowcount)  # it will count total inserted/added data
"""


# SHOW ALL RECORDS OF TABLE
"""my_cur = conn.cursor()
my_cur.execute("select * from student")
for row in my_cur:
    for data in row:
        print(data, end=" ")
    print()"""


# drop : table structure
# alter

# DELETE SINGLE DATA/ROW
"""my_cur = conn.cursor()
my_cur.execute("delete from student where rollno=2")
my_cur.execute("delete from student")   # delete all the records
if my_cur:
    print("data deleted")
else:
    print("can't delete")"""



# DELETE RECORDS
# my_cur = conn.cursor()
# my_cur.execute("delete from student where name = 'Ankit'")
# print("Total row deleted: ", my_cur.rowcount)
