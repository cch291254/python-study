from pathlib import Path
from storage import save_employee,load_employee
from business import find_employee,add_employee,update_employee,delete_employee,calculate_salary

DATA_FILE=Path(__file__).resolve().parent/"data"/"employees.json"
employees=  load_employee(DATA_FILE)
while True:
    print("1.查询所有员工")
    print("0.退出系统")
    print("2.按id查询员工")
    print("3.添加员工")
    print("4.修改员工")
    print("5.删除员工")
    print("6.计算工资")
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
    elif choice=="3":
        try:
            employee_id=int(input("请输入员工id："))
            name=input("请输入员工姓名：")
            base=int(input("请输入基本薪资："))
        except ValueError:
            print("员工id以及基本薪资必须是整数")
            continue
        if base<0:
            print("基本工资不为负数")
            continue
        new_employee={"id":employee_id,"name":name,"base":base}
        success=add_employee(employees,new_employee)
        if success:
            save_employee(employees,DATA_FILE)
            print("添加员工成功")
        else:
            print("员工id已存在")
    elif choice=="4":
        try:
            employee_id=int(input("请输入员工id："))
            new_name=input("请输入员工姓名：")
            new_base=int(input("请输入基本薪资："))
        except ValueError:
            print("员工id以及基本薪资必须是整数")
            continue
        if new_base<0:
            print("基本工资不为负数")
            continue
        success=update_employee(employees,employee_id,new_name,new_base)
        if success:
            save_employee(employees,DATA_FILE)
            print("员工修改成功")
        else:
            print("员工不存在")
    elif choice=="5":
        try:
            employee_id=int(input("请输入要删除的员工id："))
        except ValueError:
            print("员工id须为整数")
            continue
        success=delete_employee(employees,employee_id)
        if success:
            save_employee(employees,DATA_FILE)
            print("员工删除成功")
        else:
            print("员工不存在")
    elif choice=="6":
        try:
            employee_id=int(input("请输入员工id:"))
            bonus=int(input("请输入员工奖金或者扣款:"))
        except ValueError:
            print("员工id以及奖金需为整数")
            continue
        employee=find_employee(employees,employee_id)
        if employee:
            salary=calculate_salary(employee,bonus)
            print(employee["name"],"工资为:",salary)
        else:
            print("员工不存在")
    elif choice=="0":
        print("已退出系统")
        break
    else:
        print("输出选项无效")
save_employee(employees,DATA_FILE)
