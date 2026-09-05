FULL_DAY=22
FULL_BONUS=500
employees=[{"name":"张三","base":8000,"attend":22,"grade":"A"},
{"name":"李四","base":10000,"attend":20,"grade":"B"},
{"name":"王五","base":6000,"attend":22,"grade":"C"},
{"name":"赵六","base":9000,"attend":18,"grade":"A"},
{"name":"钱七","base":7000,"attend":22,"grade":"D"}]
for emp in employees:
    key=emp["name"]
    value=emp["base"]
    print(key,value)

total_salary = 0          
max_salary = 0            
max_name = ""             
min_salary = float("inf") 
min_name = ""  
for emp in employees:
    name=emp["name"]
    base=emp["base"]
    attend=emp["attend"]
    grade=emp["grade"]
    daily=base/FULL_DAY
    attend_pay=daily*attend
    if grade=="A":
        bonus=base*0.3
    elif grade=="B":
        bonus=base*0.2
    elif grade=="C":
        bonus=base*0.1
    else:
        bonus=0
    if attend==FULL_DAY:
        full_bonus=FULL_BONUS
    else:
        full_bonus=0
    salary=attend_pay+bonus+full_bonus
    print(f"{name}:考勤{attend_pay:.0f},绩效{bonus:.0f},全勤{full_bonus},实发{salary:.0f}")

    total_salary+=salary
    if salary>max_salary:
        max_salary=salary
        max_name=name
    if salary<min_salary:
        min_salary=salary
        min_name=name
avg_salary=total_salary/len(employees)
print("="*30)
print(f"总工资：{total_salary}")
print(f"平均工资：{avg_salary:.0f}")
print(f"最高工资：{max_name} {max_salary:.0f}")
print(f"最低工资：{min_name} {min_salary:.0f}")

emp_dict={emp["name"]: emp for emp in employees}
while True:
    query_name=input("请输入查询人员名字(q退出):")     
    if query_name=="q":
        print("查询结束")
        break
    if  query_name in emp_dict: 
        emp=emp_dict[query_name]  
        name = emp["name"]
        base = emp["base"]
        attend = emp["attend"]
        grade = emp["grade"]
        daily = base / FULL_DAY
        attend_pay = daily * attend
        if grade == "A":
            bonus = base * 0.3
        elif grade == "B":
            bonus = base * 0.2
        elif grade == "C":
            bonus = base * 0.1
        else:
            bonus = 0
        full_bonus = FULL_BONUS if attend == FULL_DAY else 0
        salary = attend_pay + bonus + full_bonus
        print(f"{name} 的实发工资是：{salary:.0f}") 
    else:            
        print(f"查无此人：{query_name}")



    