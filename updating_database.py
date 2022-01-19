import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database='student_db')
cursor = con.cursor()

#update the data....
marks = int(input("Enter your marks"))
name = input("Enter the name")
query = "Update info set marks={} where name= '{}'".format(marks,name)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
    print("update successfully.....")
else:
    print("No updation")