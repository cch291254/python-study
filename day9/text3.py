employees=[{"name": "张三", "salary": 8000, "age": 28},
    {"name": "李四", "salary": 12000, "age": 35},
    {"name": "王五", "salary": 6000, "age": 24},
    {"name": "赵六", "salary": 9000, "age": 30}]
names_list=[emp["name"] for emp in employees if emp["age"]>=30]
print(names_list)
names_dict={emp['name']:emp['salary'] for emp in employees}
print(names_dict)
age_list=[emp["name"] for emp in sorted(employees,key=lambda emp:emp["age"])]
print(age_list)
result=['高薪' if emp['salary']>=9000 else '普通' for emp in employees]
print(result)