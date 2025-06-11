import sqlite3
connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values('shagun', 'Data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('sharad', 'CGL', 'B',87)''')
cursor.execute('''Insert into STUDENT values('shekhar', 'physics', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('somya', 'Data Science', 'C', 67)''')

print("ALL data rows")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
    
connection.commit()
connection.close()
