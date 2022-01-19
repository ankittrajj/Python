import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ankit@8285',
                database='student_db')

cursor = con.cursor();
query = "select * from info"
cursor.execute(query)
# data = cursor.fetchone()
# data = cursor.fetchmany(2)
data = cursor.fetchall()
print(data)