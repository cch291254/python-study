class Dog:
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def introduce(self):
        print(f"我是{self.name},今年{self.age}岁，是{self.breed}")
d1=Dog("旺财",3,"田园犬")
d2=Dog("小白",2,"拉布拉多")
d3=Dog("小黑",1,"柴犬")
print(d1.name,d1.age,d1.breed)
print(d2.name,d2.age,d2.breed)
print(d3.name,d3.age,d3.breed)
d1.introduce()
d2.introduce()
d3.introduce()