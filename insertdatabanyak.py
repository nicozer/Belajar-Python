import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_buku"
)

cursor=db.cursor()

sql="INSERT INTO pelanggan (nama,alamat) VALUES (%s, %s)"
values=[
    ("BUDI", "JAKARTA"),
    ("CITRA", "BANDUNG"),
    ("DADANG", "TEGAL"),
    ("ERI", "JOMBANG"),
    ("FAHMI", "Kediri"),
]

for i in values:
    cursor.execute(sql, i)
    db.commit()

print("Data berhasil di tambahkan sebanyak {}".format(len(values)))