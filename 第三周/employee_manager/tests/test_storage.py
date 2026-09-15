

from storage import save_employee,load_employee
def test_save_and_load_employee(tmp_path):
    file_path=tmp_path/"employees.json"
    employees = [
        {"id": 1, "name": "张三", "base": 8000},
        {"id": 3, "name": "王五", "base": 6500}
    ]
    save_employee(employees,file_path)
    result=load_employee(file_path)
    assert result==employees
def test_load_employee_file_not_found(tmp_path):
    file_path=tmp_path/"missimg.json"
    result=load_employee(file_path)
    assert result==[]
def test_load_employee_broken_json(tmp_path):
    file_path = tmp_path / "broken.json"

    file_path.write_text("这不是JSON", encoding="utf-8")

    result = load_employee(file_path)

    assert result == []