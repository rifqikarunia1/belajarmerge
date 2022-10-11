from sqlite3 import Cursor
import mysql.connector as mysql

db = mysql.connect(
    host ="localhost",
    user = "user",
    passwd = ""
)

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "data_buku"
)

Cursor = db.cursor()
sql = "UPDATE buku SET judul=%s, penulis=%s WHERE id_buku=%s"
val = ("Si Kemod", "Jujun", 1)
Cursor.execute(sql, val)

db.commit()

print ("{} data diubah".format(Cursor.rowcount))