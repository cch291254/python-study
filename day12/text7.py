from pathlib import Path

from storage import save_employee_data, load_employee_data

class Employee:
    def __init__(self,name,department):
        self.name=name
        self.department=department
    def to_dict(self):
        return{"name":self.name,"department":self.department}
employees=[Employee("张三","工程"),Employee("李四","工程"),Employee("王五","财务")]
employees_data=[]
for emp in employees:
    employees_data.append(emp.to_dict())

data_file=Path("department_employees.json")
if data_file.exists():
     loaded_data = load_employee_data(data_file)
else:
    save_employee_data(employees_data,data_file)
    loaded_data = employees_data

loaded_employees=[]
for data in loaded_data:
    employee=Employee(data["name"],data["department"])
    loaded_employees.append(employee)
for employee in loaded_employees:
    print(f"{employee.name}：{employee.department}")

