
import business
import database


def show_all_employees():
    employees=database.get_all_employee()
    if employees:
        print("当前员工：")

        for employee in employees:
            print(
                "员工ID：", employee[0],
                "姓名：", employee[1],
                "基本工资：", employee[2]
            )
    else:
        print("暂无员工")
def show_employee_by_id():
    try:
        employee_id=int(input("请输入员工id："))
    except ValueError:
        print("员工输入需要为整数")
        return
    employee=database.get_employee_by_id(employee_id)
    if employee:
        print("员工ID：", employee[0],
            "姓名：", employee[1],
            "基本工资：", employee[2])
    else:
        print("员工不存在")
def add_employee_from_input():
    try:
        employee_id=int(input("请输入员工id："))
        name=input("请输入员工姓名:")
        base=int(input("请输入基本工资："))
    except ValueError:
        print("员工id和工资需为整数")
        return
    if base<0:
        print("工资不能为负")
        return
    success=database.add_employee(employee_id,name,base)
    if success:
        print("员工添加成功")
    else:
        print("员工id已存在")
def update_employee_from_input():
    try:
        employee_id = int(input("请输入要修改的员工ID："))
        new_name = input("请输入新的员工姓名：")
        new_base = int(input("请输入新的基本工资："))
    except ValueError:
        print("员工id和工资需为整数")
        return
    if new_base<0:
        print("工资不为负")
        return
    success=database.update_employee(employee_id,new_name,new_base)
    if success:
        print("员工已修改")
    else:
        print("员工不存在")
def delete_employee_from_input():
    try:
        employee_id = int(input("请输入要删除的员工ID："))
    except ValueError:
        print("员工ID必须是整数")
        return

    success = database.delete_employee(employee_id)
    if success:
        print("员工删除成功")
    else:
        print("员工不存在")
def calculate_salary_from_input():
    try:
        employee_id=int(input("请输入员工id："))
        bonus=int(input("请输入奖金或者扣款："))
    except ValueError:
        print("员工id和工资需为整数")
        return
    employee=database.get_employee_by_id(employee_id)

    if employee is None:
        print("员工不存在")
        return
    employee_data={"id":employee[0],
    "name":employee[1],
    "base":employee[2]}
    salary=business.calculate_salary(employee_data,bonus)
    print(employee_data["name"],"工资为：",salary)
def main():

    database.init_db()
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
            show_all_employees()
        elif choice=="0":
            print("已退出系统")
            break
        elif choice=="2":
            show_employee_by_id()
        elif choice=="3":
            add_employee_from_input()
        elif choice=="4":
            update_employee_from_input()
        elif choice=="5":
            delete_employee_from_input()
        elif choice=="6":
            calculate_salary_from_input()
        else:
            print("输出选项无效")
if __name__=="__main__":
    main()