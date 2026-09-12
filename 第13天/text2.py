import json

try:
    with open("broken_salary.json", "r", encoding="utf-8") as file:
        salary_data=json.load(file)
    print(salary_data)
except json.JSONDecodeError:
    print("工资数据格式错误")