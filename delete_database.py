import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database='ankit')

cursor = con.cursor();
name = input("Enter the name:-")
query = "delete from student where name = '{}'".format(name)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
    print("Data deleted successfully.......")
else:
    print("No data deleted.....")