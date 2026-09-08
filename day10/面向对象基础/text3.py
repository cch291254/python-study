FULL_DAY=22
FULL_BONUS=500
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

e1 = Employee("张三", 8000, 22, "A")
print(f"{e1.name} 的月薪：{e1.calc_salary():.0f}")  
e2 = Employee("李四", 10000, 20, "B")
print(f"{e2.name} 的月薪：{e2.calc_salary():.0f}")  

