import json
class Employee:
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def to_dict(self):
        return{"name":self.name,"department":self.department}
employee=Employee("张三","工程")
with open("one_employee.json","w",encoding="utf-8")as f:
    json.dump(employee.to_dict(),f,ensure_ascii=False,indent=2)
with open("one_employee.json", "r", encoding="utf-8") as file:
    employee_r = json.load(file)
new_employee=Employee(employee_r["name"],employee_r["department"])
print(f"员工{new_employee.name}属于{new_employee.department}部门")

