colors=["red", "green", "blue"]
a=[f"{i}：{color}" for i,color in enumerate(colors)]
print(a)


students=["张三","李四","王五"]
scored=[88,76,93]
stu_scored=[f"{name}的分数是{score}" for name,score in zip(students,scored)]
print(stu_scored)


keys = ['a', 'b', 'c']
values = [1, 2, 3]
nums=dict(zip(keys,values))
print(nums)

cities = ['北京', '上海', '广州']
populations = [2154, 2424, 1530]  
city_popul=[f"第{j+1}个城市：{city}，人口{num}万" for j,(city,num) in enumerate(zip(cities,populations))]
print(city_popul)