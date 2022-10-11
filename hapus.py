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
sql = "DELETE FROM buku WHERE id_buku=%s"
val = (1,)
Cursor.execute(sql, val)

print("{} Data dihapus".format(Cursor.rowcount))