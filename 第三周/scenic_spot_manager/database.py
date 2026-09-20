import sqlite3
from pathlib import Path

DB_ONE=Path(__file__).parent
DB_FILE=DB_ONE/"scenic_spots.db"
def init_db():
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS scenic_spots(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL ,
    city text not null,
    price REAL NOT NULL )""")
    conn.commit()
    conn.close()
def add_spot(spot_id,name,city,price):
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    try:
        cursor.execute("INSERT INTO scenic_spots(id,name,city,price) values (?,?,?,?)",(spot_id,name,city,price))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        conn.rollback()
        return False
    finally:
        conn.close()
def get_all_spots():
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute("SELECT*FROM scenic_spots ORDER BY id asc")
    scenic_spots=cursor.fetchall()
    conn.close()
    return scenic_spots
def get_spot_by_id(spot_id):
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute("SELECT*FROM scenic_spots where id=?",(spot_id,))
    scenic_spot=cursor.fetchone()
    conn.close()
    return scenic_spot 
def update_spot_price(spot_id,new_price):
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute("UPDATE scenic_spots set price=? where id=?",(new_price,spot_id))
    conn.commit()
    success=cursor.rowcount==1
    conn.close()
    return success
def delete_spot(spot_id):
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute("delete FROM scenic_spots WHERE id=?",(spot_id,))
    conn.commit()
    success=cursor.rowcount==1
    conn.close()
    return success
