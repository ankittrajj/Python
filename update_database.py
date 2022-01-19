import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database='student_db')
cursor = con.cursor()
# name = input("Enter the name:- ")
# marks = int(input("Enter new marks:- "))
# age = int(input("Enter the age:-"))
# query = "delete from info  where age=23"
# query = "update info set age={} where name='{}'".format(age,name)
# query2 = "update info set marks=0 where name='asd'"

# extraction of data
query = "select * from info"
cursor.execute(query)
data = cursor.fetchall()
print(data)
# cursor.execute(query2)

# con.commit()
#
# if cursor.rowcount>0:
#     print("Updated.....")
# else:
#     print("No updation occur")