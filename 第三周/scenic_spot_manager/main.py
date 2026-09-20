
import database
def show_all_spots():
    scenic_spots=database.get_all_spots()
    if scenic_spots:
        print("当前景点：")
        for spot in scenic_spots:
            print("景区编号：",spot[0])
            print("名称：",spot[1])
            print("所在城市：",spot[2])
            print("预算：",spot[3])
    else:
        print("暂无景点") 
def show_one_spot_by_id():
    try:
        spot_id=int(input("请输入景区编号:"))
    except ValueError:
        print("编号输入需要为整数")
        return
    spot=database.get_spot_by_id(spot_id)
    if spot:
        print("景区名称：",spot[1])
        print("所在城市：",spot[2])
        print("价格：",spot[3])
    else:
        print("查询不到该景区")
def add_new_spot():
    try:
        id=int(input("请输入景区编号;"))
        name=input("名称：")
        city=input("城市：")
        price=float(input("价格："))
    except ValueError:
        print("景区编号需要为整数，预算需要为整数或者小数")
        return
    if price<0:
        print("价格不可为负数")
        return
    success=database.add_spot(id,name,city,price)
    if success:
        print("景区添加成功") 
    else:
        print("景区id已存在")
def updata_spot_price():
    try:
        id=int(input("请输入景区编号："))
        new_price=float(input("请输入价格："))
    except ValueError:
        print("景区编号需要为整数，预算需要为整数或者小数")
        return
    if new_price<0:
        print("价格不可为负数")
        return
    success=database.update_spot_price(id,new_price)
    if success:
        print("修改成功")
    else:
        print("景区不存在")
def delete_spot_by_id():
    try:
        id=int(input("请输入景区编号"))
    except ValueError:
        print("编号需要为整数")
        return
    success=database.delete_spot(id)
    if success:
        print("删除成功")
    else:
        print("景区不存在")
def main():
    database.init_db()
    while True:
        print("1.查询所有景点")
        print("2.按id查询景点")
        print("3.添加景点")
        print("4.修改景点价格")
        print("5.删除景点")
        print("0.退出系统")
        choice=input("请选择功能：")
        if choice=="1":
            show_all_spots()
        elif choice=="0":
            print("谢谢使用")
            break
        elif choice=="2":
            show_one_spot_by_id()
        elif choice=="3":
            add_new_spot()
        elif choice=="4":
            updata_spot_price()
        elif choice=="5":
            delete_spot_by_id()
        else:
            print("选项不存在")
if __name__=="__main__":
    main()

