import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'student_db')

cursor = con.cursor()
while True:
    name = input("Enter your name")
    age = int(input("Enter your age"))
    marks = float(input("Enter your marks"))

    query = "Insert into info values('{}',{},{})".format(name,age,marks)
    cursor.execute(query)
    con.commit()
    print("Data entered successfully")

    option = int(input("Enter your choice\n 1. Enter more Data\n 2.Exit"))
    if option == 2:
        break










# if con.is_connected():
#     print("Database connected successfully")