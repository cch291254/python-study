employees = [
    {"name": "张三", "base": 8000, "attend": 22, "grade": "A"},
    {"name": "李四", "base": 10000, "attend": 20, "grade": "B"},
    {"name": "王五", "base": 6000, "attend": 22, "grade": "C"},
    {"name": "赵六", "base": 9000, "attend": 18, "grade": "A"},
    {"name": "钱七", "base": 7000, "attend": 22, "grade": "D"},
]

def filter_and_sum(employees,grade):
    total=0
    names=[]
    for emp in employees:
        if emp["grade"]==grade:
            total+=emp["base"]
            names.append(emp["name"])
    return names,total
print(filter_and_sum(employees, "A"))
print(filter_and_sum(employees, "D"))
    