import sqlite3


db = sqlite3.connect('sql.db')
cur = db.cursor()
#  Создание первой таблицы       Имя 
## СЛЕДИ ЗА ЗНАЧЕНИЯМИ ТЕКСТ ИЛИ ИНТЕДЖЕР

cur.execute('''CREATE TABLE table1 (
id INTEGER PRIMARY KEY,
login TEXT NOT NULL,
data text not null,
name text not null,
ball text
)''')