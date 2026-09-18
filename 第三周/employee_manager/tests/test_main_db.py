import main_db
def test_show_all_employees(monkeypatch,capsys):
    test_employees=[(1,"张三",8000),(2,"李四",10000),]
    monkeypatch.setattr(main_db.database,"get_all_employee",lambda:test_employees)
    main_db.show_all_employees()
    output=capsys.readouterr().out
    assert "当前员工" in output
    assert "张三" in output
    assert "8000" in output
    assert "李四" in output
    assert "10000" in output
def test_show_al_employees_empty(monkeypatch,capsys):
    monkeypatch.setattr(main_db.database,"get_all_employee",lambda:[])
    main_db.show_all_employees()
    output=capsys.readouterr().out
    assert "暂无员工" in output   
def test_show_employee_by_id_found(monkeypatch,capsys):
    monkeypatch.setattr("builtins.input",lambda messge:"3")
    monkeypatch.setattr(main_db.database,"get_employee_by_id",lambda employee_id:(3,"王五",6800))
    main_db.show_employee_by_id()
    output=capsys.readouterr().out
    assert "王五" in output
    assert "6800" in output
def test_shhow_employee_by_id_not_found(monkeypatch,capsys):
    monkeypatch.setattr("builtins.input",lambda messge:"99")
    monkeypatch.setattr(main_db.database,"get_employee_by_id",lambda employee_id:None)
    main_db.show_employee_by_id()
    output=capsys.readouterr().out
    assert "员工不存在" in output
def test_show_employee_by_id_invalid_input(monkeypatch,capsys):
    monkeypatch.setattr("builtins.input",lambda messga:"abc")
    main_db.show_employee_by_id()
    output=capsys.readouterr().out
    assert "员工输入需要为整数" in output
