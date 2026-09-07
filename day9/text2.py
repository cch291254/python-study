employees = [
    {"name": "张三", "salary": 8000},
    {"name": "李四", "salary": 12000},
    {"name": "王五", "salary": 6000},
    {"name": "赵六", "salary": 9000}]
salary_list=sorted(employees,key=lambda emp:emp["salary"],reverse=True) 
print(salary_list)
salary_max=max(employees,key=lambda emp:emp["salary"])
print(salary_max)


names = ["赵六", "张三丰", "欧阳娜娜", "王"]
names_list=sorted(names,key=lambda name:len(name))
print(names_list)