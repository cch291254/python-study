from unittest import result


employees = [
    {"name": "张三", "salary": 8000, "age": 28},
    {"name": "李四", "salary": 12000, "age": 35},
    {"name": "王五", "salary": 6000, "age": 24},
    {"name": "赵六", "salary": 9000, "age": 30}]
def analyze_employees(employees, min_salary=8000):
    high_emps=[emp for emp in employees if emp["salary"]>=8000]
    sorted_emps=sorted(high_emps,key=lambda kfc: kfc["salary"], reverse=True)
    top= max(high_emps,key=lambda kfc:kfc["salary"])
    high_nums=len(high_emps)
    total_salary=sum(emp['salary'] for emp in high_emps)
    return {"人数": high_nums,
        "工资总和": total_salary,
        "最高工资员工": top["name"],
        "最高工资": top["salary"],
        "高薪员工名单": [emp["name"] for emp in sorted_emps]}
result=analyze_employees(employees)
print(result)




