try:
    with open("salary_history.json","r",encoding="utf-8")as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("工资历史文件不存在")

