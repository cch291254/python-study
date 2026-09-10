from pathlib import Path
a_path=Path("employees.json")
if a_path.exists():
    print("员工文件存在")
else:
    print("找不到员工文件")
    
