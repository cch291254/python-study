import sqlite3
from pathlib import Path

DB_FILE=Path(__file__).resolve().parent/"employees.db"
def init_db():
    connection=sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(          
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    base INTEGER NOT NULL)""")
    connection.commit()
    connection.close()
def get_all_employee():
    connection=sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute("select*from employees")
    employees=cursor.fetchall()
    connection.close()
    return employees
def add_employee(employee_id,name,base):
    connection=sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    try:
        cursor.execute("insert into employees(id,name,base) values (?,?,?)",(employee_id,name,base))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        connection.rollback()
        return False
    finally:
        connection.close()
def get_employee_by_id(employee_id):
    connection=sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute("select*from employees where id=?",(employee_id,))
    employee=cursor.fetchone()
    connection.close()
    return employee
def update_employee(employee_id,new_name,new_base):
    connection=sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute("update employees set name=?,base=? where id=?",(new_name,new_base,employee_id))
    connection.commit()
    success=cursor.rowcount==1
    connection.close()
    return success
def delete_employee(employee_id):
    connection=sqlite3.connect(DB_FILE)
    cursor=connection.cursor()
    cursor.execute("delete from employees where id=?",(employee_id,))
    connection.commit()
    success=cursor.rowcount==1
    connection.close()
    return success
if __name__=="__main__":
    init_db()
    employees=get_all_employee()
    print(employees)
