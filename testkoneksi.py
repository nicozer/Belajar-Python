import mysql.connector

db=mysql.connector.connet(
    host="localhost"
    user="admin"
    passwd="admin"
)

if db.is_connected():
    print("database connect")
else:
    print("database tidak konek")