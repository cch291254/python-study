
def find_employee(employees,employee_id):
    for employee in employees:
        if employee["id"]==employee_id:
            return employee
    return None
def add_employee(employees,employee):
    if employee["base"]<0:
        return False
    if find_employee(employees,employee["id"]):
        return False
    employees.append(employee)
    return True
def update_employee(employees,employee_id,new_name,new_base):
    if new_base<0:
        return False
    employee=find_employee(employees,employee_id)

    if employee is None:
        return False
    employee["name"]=new_name
    employee["base"]=new_base
    return True
def delete_employee(employees,employee_id):
    employee=find_employee(employees,employee_id)
    if employee is None:
        return False
    employees.remove(employee)
    return True
def calculate_salary(employee,bonus=0):
    return employee["base"]+bonus
