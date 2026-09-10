from pathlib import Path

from day12.衔接检查 import employees
data_dir=Path("records")
file_path=data_dir/"empoloyee_data.json"
print(file_path)

if file_path.exists():
    print("找到员工数据")
else:
    print("员工数据不存在")


