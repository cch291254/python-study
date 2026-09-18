# 员工管理系统

这是一个使用 Python 编写的命令行员工管理项目，使用 SQLite 保存员工数据。

## 功能

- 查询所有员工
- 按员工 ID 查询
- 添加员工
- 修改员工
- 删除员工
- 根据基本工资和奖金计算工资
- 处理无效输入和重复员工 ID

## 项目结构

- `main_db.py`：命令行界面和用户输入
- `database.py`：SQLite 数据库操作
- `business.py`：工资计算等业务规则
- `storage.py`：JSON 文件存储功能
- `tests/`：pytest 自动化测试

## 运行项目

进入项目目录后运行：

```powershell
python main_db.py
```

程序会自动创建 SQLite 数据库文件。

## 运行测试

```powershell
python -m pytest -v
```

当前测试结果：

```text
26 passed
```

## 使用技术

- Python
- SQLite
- JSON
- pytest
- Git

