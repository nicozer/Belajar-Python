import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_buku"
)

cursor=db.cursor()
sql="SELECT * FROM pelanggan"
cursor.execute(sql)

result=cursor.fetchall() #untuk menampilkan semua data yang ada
# result=cursor.fetchone untuk menampilkan satu data teratas
# result=cursor.fetchmany(10) untuk menampilkan banyaknya data sesuai yang di butuhkan contoh 10
for data in result:
    print(data)