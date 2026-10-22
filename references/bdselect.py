import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("uley3_0.db")

conn = sqlite3.connect(DB)
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()
for row in cur.execute("SELECT id_uley, name FROM sensor"):
    print(row)
for row2 in cur.execute("SELECT name, rtime, date, units FROM sensor"):
    print(row2)
conn.commit()
conn.close()                                     