#create database name and specififed in db variable
import pymysql
Semester I- Research in Computing
6
db = pymysql.connect("localhost","root","123456","mydb1" )
cursor = db.cursor()
sql = """SELECT * from TEST"""
try:
cursor.execute(sql)
results = cursor.fetchall()
# Now print fetched result
for row in results:
print(row)
print("success")
db.commit()
except:
db.rollback()
db.close()
