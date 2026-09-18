#SQL 咨询、排序与统计练习
import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        base INTEGER NOT NULL
    )
""")

employees = [
    (1, "张三", "技术部", 8000),
    (2, "李四", "市场部", 6500),
    (3, "王五", "技术部", 9000),
    (4, "赵六", "人事部", 7000),
    (5, "陈七", "技术部", 7500),
]

for employee in employees:
    cursor.execute(
        "INSERT INTO employees VALUES (?, ?, ?, ?)",
        employee
    )

conn.commit()
cursor.execute("SELECT name,base FROM employees")
result=cursor.fetchall()
print("全部学院：",result)
cursor.execute("SELECT name,base FROM employees WHERE department=?",("技术部",))
result=cursor.fetchall()
print("技术部员工：",result)
# 在这里独立完成 5 条查询
cursor.execute("SELECT name,base FROM employees ORDER BY base ASC")
result=cursor.fetchall()
print("工资升序：",result)
cursor.execute("SELECT name,base FROM employees ORDER BY base DESC")
result=cursor.fetchall()
print("工资降序：",result)
cursor.execute("SELECT name,base FROM employees ORDER BY base ASC LIMIT 2")
result=cursor.fetchall()
print("工资最低两人：",result)
cursor.execute("SELECT name,base FROM employees ORDER BY base DESC LIMIT 3")
result=cursor.fetchall()
print("工资最高的员工：",result)
cursor.execute("SELECT COUNT(*) FROM employees WHERE department=?",("技术部",))
result=cursor.fetchone()
print("技术部人数总数：",result)
cursor.execute("SELECT department,COUNT(*) FROM employees GROUP BY department ORDER BY COUNT(*) DESC")
result=cursor.fetchall()
print("各部门人数：",result)
conn.close()