import json
employees=[{"name":"张三","department":"工程"},{"name":"李四","department":"工程"}]
with open ("employees.json","w",encoding="utf-8") as f:
    json.dump(employees,f,ensure_ascii=False,indent=2)
with open("employees.json","r",encoding="utf-8")as f :
    loaded_employees=json.load(f)
print(len(loaded_employees))
loaded_employees.append({"name":"王五","department":"财务"})
with open ("employees.json","w",encoding="utf-8") as f:
    json.dump(loaded_employees,f,ensure_ascii=False,indent=2)
with open("employees.json","r",encoding="utf-8")as f :
    loaded_employees=json.load(f)
for emp in loaded_employees:
    name=emp["name"]
    department=emp["department"]
    print(name,department)