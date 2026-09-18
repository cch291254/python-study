import sqlite3

conn=sqlite3.connect(":memory:")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE employees(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
base INTEGER NOT NULL)""")
cursor.execute("INSERT INTO employees VALUES (?,?,?)",(1,"张三",8000))
conn.commit()
try:
    cursor.execute("UPDATE employees SET base=? WHERE id=?",(9000,1))
    cursor.execute("INSERT INTO employees VALUES(?,?,?)",(2,"李四",7000))
    conn.commit()
except sqlite3.IntegrityError:
    conn.rollback()
    print("操作失败，已回滚")
cursor.execute("SELECT id,name,base FROM employees ORDER BY id DESC")
result=cursor.fetchall()
print("提交后的员工：",result)
cursor.execute("DELETE FROM employees WHERE id=?",(2,))
conn.commit()
cursor.execute("SELECT id,name,base FROM employees ORDER BY id DESC")
result=cursor.fetchall()
print("剩余员工：",result)
conn.close()