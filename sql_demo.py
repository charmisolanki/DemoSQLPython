import mysql.connector
from mysql.connector import connect
from pip._vendor.distlib import database

connection = connect(host = 'localhost' , user = 'root' , passwd = 'Charmi@02' , database = 'demodb' )

my_cursor = connection.cursor()

# insert_query = "INSERT INTO student (name, college) VALUES (%s, %s) "
# vals = ('shilpa' , 'Raheja')
# my_cursor.execute(insert_query, vals)
# connection.commit()

# delete_query = "DELETE FROM student WHERE name = %s"
# val = ("shilpa", )
# my_cursor.execute(delete_query, val)
# connection.commit()

# like_query = "SELECT * FROM student WHERE college LIKE '%raheja%'"
# my_cursor.execute(like_query)

# update_query = "UPDATE student SET college = %s WHERE name = 'shilpa'"
# val = ("NM college", )
# my_cursor.execute(update_query, val)
# connection.commit()

my_cursor.execute("select * from student")
result = my_cursor.fetchall()
for i in result:
    print(i)