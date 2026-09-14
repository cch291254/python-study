


from business import find_employee,add_employee,update_employee,delete_employee
employees = [
    {"id": 1, "name": "张三", "base": 8000},
    {"id": 2, "name": "李四", "base": 10000}
]
def test_find_employee():
    result=find_employee(employees,2)
    assert result["name"]=="李四"
    assert result["base"]==10000
def test_employee_not_found():
    result=find_employee(employees,90)
    assert result is None
def test_add_employee():
    employees = [
    {"id": 1, "name": "张三", "base": 8000},
    {"id": 2, "name": "李四", "base": 10000}]
    new_employee={"id":3,"name":"王五","base":6000}
    result=add_employee(employees,new_employee)
    assert result is True
    assert len(employees)==3
    assert employees[2]["name"]=="王五"
def test_add_dunplicate_id():
    employees = [
    {"id": 1, "name": "张三", "base": 8000},
    {"id": 2, "name": "李四", "base": 10000}]
    dup_employee={"id":2,"name":"王五","base":6000}
    result=add_employee(employees,dup_employee)
    assert result is False
    assert len(employees)==2
def test_update_employee():
     employees = [
    {"id": 1, "name": "张三", "base": 8000},
    {"id": 2, "name": "李四", "base": 10000}]
     result=update_employee(employees,2,"李四",12000)
     assert result is True
     assert employees[1]["base"]==12000
def test_update_employee_not_found():
    employees = [
    {"id": 1, "name": "张三", "base": 8000},
    {"id": 2, "name": "李四", "base": 10000}]
    result=update_employee(employees,99,"李四",120000)
    assert result is False
    assert employees[0]["base"]==8000
    assert employees[1]["base"]==10000
def test_delete_employee():
    employees = [
    {"id": 1, "name": "张三", "base": 8000},
    {"id": 2, "name": "李四", "base": 10000}]
    result=delete_employee(employees,2)
    assert result is True
    assert len(employees)==1
def test_delete_employee_not_found():
    employees = [
    {"id": 1, "name": "张三", "base": 8000},
    {"id": 2, "name": "李四", "base": 10000}]
    result=delete_employee(employees,99)
    assert result is False
    assert len(employees)==2
    assert employees[1]["name"]=="李四"
