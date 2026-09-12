import json

def load_employee_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("员工数据文件不存在")
        return []
    except json.JSONDecodeError:
        print("员工数据格式错误")
        return []
assert load_employee_data("missing.json")==[]
assert load_employee_data("broken_salary.json")==[]
data=load_employee_data("normal_salary.json")
assert data["name"]=="李四"
assert data["salary"]==12500
print("全部测试过")
data=load_employee_data("normal_salary.json")
if data:
    print(data["salary"])
else:
    print("没有可用工资数据")