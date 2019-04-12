import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_buku"
)

cursor = db.cursor()
sql="INSERT INTO pelanggan (nama,alamat) VALUES (%s, %s)"
val=("BAMBANG", "Surabaya")
cursor.execute(sql,val)
db.commit()

print("Data Berhasil Di Inputkan")