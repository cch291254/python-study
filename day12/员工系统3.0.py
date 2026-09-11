from pathlib import Path

from storage import save_employee_data, load_employee_data

class Employee:
    FULL_BONUS=500
    FULL_DAY=22
    def __init__(self,name,base,attend,grade):
        self.name = name
        self._base = base
        self._attend = attend
        self._grade = grade
    def __str__(self):
        return f"员工{self.name}：底薪{self._base}，出勤{self._attend}天，绩效{self._grade}"
    def calc_salary(self):
        daily_pay=self._base/Employee.FULL_DAY
        attend_pay=daily_pay*self._attend
        if self._grade=="A":
            bonus=self._base*0.3
        elif self._grade == "B":
            bonus = self._base * 0.2
        elif self._grade == "C":
            bonus = self._base * 0.1
        else:
            bonus = 0
        full_bonus=Employee.FULL_BONUS if self._attend==Employee.FULL_DAY else 0
        return attend_pay+full_bonus+bonus
    def calc_annual_salary(self, months=12):
        return self.calc_salary() * months
    def get_salary(self):
        return self._salary
    def get_base(self):
        return self._base
    def get_grade(self):
        return self._grade
    def to_dict(self):
        return {
        "name": self.name,
        "base": self._base,
        "attend": self._attend,
        "grade": self._grade}

employees = [
    Employee("张三", 8000, 22, "A"),
    Employee("李四", 10000, 20, "B"),
    Employee("王五", 6000, 22, "C"),
    Employee("赵六", 9000, 18, "A"),
    Employee("钱七", 7000, 22, "D")]
employees_data=[]
for emp in employees:
    employees_data.append(emp.to_dict())
data_file=Path("employee_obj.json")
if data_file.exists():
    loaded_data=load_employee_data(data_file)
else:
    save_employee_data(employees_data,data_file)
    loaded_data=employees_data
loaded_employees=[]
for data in loaded_data:
    employee = Employee(
        data["name"],
        data["base"],
        data["attend"],
        data["grade"])
    loaded_employees.append(employee)
employees=loaded_employees
max_salary=0
max_name=""
min_name=""
min_salary=float("inf")
total=0
for emp in employees:
    print(f"{emp.name}:实发{emp.calc_salary():.0f}")
    total+=emp.calc_salary()
    
    if emp.calc_salary()>max_salary:
        max_name=emp.name
        max_salary=emp.calc_salary()
        
    if emp.calc_salary()<min_salary:
        min_name=emp.name
        min_salary=emp.calc_salary()
avg_salary=total/len(employees)
print(f"总支出：{total:.0f}")
print(f"平均：{avg_salary:.0f}")
print(f"最高：{max_name} {max_salary:.0f}")
print(f"最低:{min_name} {min_salary:.0f}")

emp_dict={emp.name:emp  for emp in employees}
while True:
    query=input("\n请输入姓名,按q退出:")
    if query=="q":
        print("再见")
        break
    if query in emp_dict:
        emp = emp_dict[query]
        print(f"{emp.name}：月薪{emp.calc_salary():.0f}，年薪{emp.calc_annual_salary():.0f}")
    else:
        print("查无此人")

class Intern(Employee):
    def __init__(self,name,attend,daily_pay=120):
        super().__init__(name,0,attend,"实习")
        self._daily_pay=daily_pay
    def calc_salary(self):
        return self._attend*self._daily_pay
e1 = Employee("张三", 8000, 22, "A")
i1 = Intern("小李", 20)             
i2 = Intern("小王", 18, 150)
print(e1.calc_salary())
print(i1.calc_salary())
print(i2.calc_salary())
print(i1.name)
print(i1)
print(i1.calc_annual_salary())


