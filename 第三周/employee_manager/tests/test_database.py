from dataclasses import dataclass
from unittest import result
import database
def test_add_and_get_employee(tmp_path,monkeypatch):
    test_db=tmp_path/"test_employees.db"
    monkeypatch.setattr(database,"DB_FILE",test_db)
    database.init_db()
    result=database.add_employee(1,"张三",8000)
    employee=database.get_employee_by_id(1)
    assert result is True
    assert employee==(1,"张三",8000)
def test_add_duplicate_id(tmp_path,monkeypatch):
    test_db=tmp_path/"test_employees.db"
    monkeypatch.setattr(database,"DB_FILE",test_db)
    database.init_db()
    first_result=database.add_employee(1,"张三",8000)
    second_result=database.add_employee(1,"李四",10000)
    employees=database.get_all_employee()
    assert first_result is True
    assert second_result is False
    assert employees==[(1,"张三",8000)]
def test_update_employee(tmp_path,monkeypatch):
    test_db=tmp_path/"test_employees.db"
    monkeypatch.setattr(database,"DB_FILE",test_db)
    database.init_db()
    database.add_employee(1,"张三",8000)
    result=database.update_employee(1,"张三",8500)
    employee=database.get_employee_by_id(1)
    assert result is True
    assert employee==(1,"张三",8500)
def test_update_employee_not_found(tmp_path, monkeypatch):
    test_db = tmp_path / "test_employees.db"
    monkeypatch.setattr(database, "DB_FILE", test_db)

    database.init_db()
    database.add_employee(1, "张三", 8000)
    result = database.update_employee(99, "测试", 5000)
    employee = database.get_employee_by_id(1)

    assert result is False
    assert employee == (1, "张三", 8000)
def test_delete_employee(tmp_path, monkeypatch):
    test_db = tmp_path / "test_employees.db"
    monkeypatch.setattr(database, "DB_FILE", test_db)

    database.init_db()
    database.add_employee(1,"张三",8000)
    database.add_employee(2,"李四",10000)
    result=database.delete_employee(1)
    employees=database.get_all_employee()
    assert result is True
    assert employees==[(2,"李四",10000)]
def test_delete_employee_not_found(tmp_path, monkeypatch):
    test_db = tmp_path / "test_employees.db"
    monkeypatch.setattr(database, "DB_FILE", test_db)

    database.init_db()
    database.add_employee(1,"张三",8000)
    result=database.delete_employee(99)
    employees=database.get_all_employee()
    assert result is False
    assert employees==[(1,"张三",8000)]
