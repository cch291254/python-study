
FULL_BONUS=500
FULL_DAY=22
class Employee:
    def __init__(self,name,base,attend,grade):
        self.name = name
        self.base = base
        self.attend = attend
        self.grade = grade
    def calc_salary(self):
        daily=self.base/FULL_DAY
        attend_pay=daily*self.attend
        if self.grade=="A":
            bonus=self.base*0.3
        elif self.grade == "B":
            bonus = self.base * 0.2
        elif self.grade == "C":
            bonus = self.base * 0.1
        else:
            bonus = 0
        full_bonus=FULL_BONUS if self.attend==FULL_DAY else 0
        return attend_pay+full_bonus+bonus
    def calc_annual_salary(self, months=12):
        return self.calc_salary() * months
    
employees = [
    Employee("张三", 8000, 22, "A"),
    Employee("李四", 10000, 20, "B"),
    Employee("王五", 6000, 22, "C"),
    Employee("赵六", 9000, 18, "A"),
    Employee("钱七", 7000, 22, "D")]
max_salary=0
max_name=""
min_name=""
min_salary=float("inf")
total=0
for emp in employees:
    salary=emp.calc_salary()
    print(f"{emp.name}:实发{salary:.0f}")
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