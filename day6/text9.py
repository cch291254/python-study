employees = [
    {"name": "张三", "salary": 8000, "department": "技术部"},
    {"name": "李四", "salary": 12000, "department": "技术部"},
    {"name": "王五", "salary": 7500, "department": "市场部"},
    {"name": "赵六", "salary": 9000, "department": "技术部"},
    {"name": "钱七", "salary": 6800, "department": "市场部"}]
total=0
count=0
for i in employees:
    if i["department"]=="技术部":
        total+=i["salary"]
        count+=1
print(f"技术部共{count}人，总工资{total}元")        