# 满勤天数、满勤奖做成常量：后面计算会反复用到，改规则时只改这一处
FULL_DAY = 22
FULL_BONUS = 500

# 用「字典列表」存员工：每个人是一个字典，字段名当钥匙，后面用 emp["name"] 取值
employees = [
    {"name": "张三", "base": 8000, "attend": 22, "grade": "A"},
    {"name": "李四", "base": 10000, "attend": 20, "grade": "B"},
    {"name": "王五", "base": 6000, "attend": 22, "grade": "C"},
    {"name": "赵六", "base": 9000, "attend": 18, "grade": "A"},
    {"name": "钱七", "base": 7000, "attend": 22, "grade": "D"},
]


def clac_salary(emp):
    """计算单个员工的工资组成
    参数：emp - 员工字典（含 name/base/attend/grade）
    返回：工资组成字典
    """
    # 从字典里取出字段，后面计算更短、更清楚，避免反复写 emp["xxx"]
    name = emp["name"]
    base = emp["base"]
    attend = emp["attend"]
    grade = emp["grade"]

    # 日薪 = 底薪 / 满勤天数；出勤工资按实际出勤天数折算，没来就按天扣
    daily = base / FULL_DAY
    attend_pay = daily * attend

    # 绩效奖按等级用 if-elif-else：互斥条件只命中一条，D 和未知等级走 else 为 0
    if grade == "A":
        bonus = base * 0.3
    elif grade == "B":
        bonus = base * 0.2
    elif grade == "C":
        bonus = base * 0.1
    else:
        bonus = 0

    # 只有出勤刚好等于满勤天数才给满勤奖，少一天都不给
    if attend == FULL_DAY:
        full_bonus = FULL_BONUS
    else:
        full_bonus = 0

    # 实发 = 出勤工资 + 满勤奖 + 绩效奖
    salary = attend_pay + full_bonus + bonus

    # 返回字典而不是只 print：调用方既能打印，也能继续拿字段做别的事
    return {
        "name": name,
        "attend_pay": attend_pay,
        "bonus": bonus,
        "full_bonus": full_bonus,
        "salary": salary,
    }


# 先给合计、最高、最低准备初始值；最低用正无穷，保证第一个人一定能换上去
total_salary = 0
max_salary, max_name = 0, ""
min_salary, min_name = float("inf"), ""

# 遍历所有员工：每人调一次函数，既打印明细，又顺带更新统计
for emp in employees:
    result = clac_salary(emp)
    # 键名必须和 return 里完全一致；:.0f 表示小数四舍五入成整数再显示
    print(
        f"{result['name']}：考勤{result['attend_pay']:.0f},"
        f"绩效{result['bonus']:.0f},"
        f"全勤{result['full_bonus']:.0f},"
        f"实发{result['salary']:.0f}"
    )
    total_salary += result["salary"]
    if result["salary"] > max_salary:
        max_salary = result["salary"]
        max_name = result["name"]
    if result["salary"] < min_salary:
        min_name = result["name"]
        min_salary = result["salary"]

# 这三行必须在 for 外面：等所有人都算完再打印汇总，否则会反复打印中间结果
print(f"合计：{total_salary:.0f}")
print(f"最高：{max_name} {max_salary:.0f}")
print(f"最低：{min_name} {min_salary:.0f}")

# 姓名 -> 员工字典，查询时用名字当钥匙，不用再循环找人
emp_dict = {emp["name"]: emp for emp in employees}

while True:
    # strip() 去掉首尾空格；lower() 让 Q 和 q 都能退出
    query_name = input("\n请输入要查询的员工姓名（输入 q 退出）：").strip()
    if query_name.lower() == "q":
        print("查询结束，再见！")
        break
    if query_name not in emp_dict:
        print(f"查无此人：{query_name}")
        continue

    result = clac_salary(emp_dict[query_name])   # ← 同样调用函数
    print("-" * 32)
    print(f"员工姓名：{result['name']}")
    print(f"月底薪：{emp_dict[query_name]['base']} 元")
    print(f"实际出勤：{emp_dict[query_name]['attend']} 天，考勤工资：{result['attend_pay']:.0f} 元")
    print(f"绩效等级：{emp_dict[query_name]['grade']}，绩效奖金：{result['bonus']:.0f} 元")
    print(f"全勤奖：{result['full_bonus']} 元")
    print(f"★ 实发工资：{result['salary']:.0f} 元")
    print("-" * 32)