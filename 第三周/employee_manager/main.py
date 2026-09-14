from storage import save_employee,load_employee
from business import find_employee
employees=  load_employee("data/employees.json")
while True:
    print("1.查询所有员工")
    print("0.退出系统")
    print("2.按id查询员工")
    choice=input("请选择功能：")
    if choice=="1":
        print("当前员工：")
    
        for employee in employees:
            print(employee)
    elif choice=="2":
        try:
            employee_id=int(input("请输入员工id："))
            
        except ValueError:
            print("员工id必须是整数")
            continue    
        employee=find_employee(employees,employee_id)
        if employee:
            print("查询结果：",employee)
        else:
             print("员工不存在")
    elif choice=="0":
        print("已退出系统")
        break
    else:
        print("输出选项无效")
save_employee(employees,"data/employees.json")
