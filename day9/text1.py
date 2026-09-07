def greet(name,greeting="你好"):
    return f"{greeting},{name}!"
print(greet("张三"))
print(greet("李四","早上好"))


def calc_avg(*nums):
    total=0
    for num in nums:
        total+=num
        avg=total/len(nums)
    return avg
print(calc_avg(80,90,100))
print(calc_avg(1,2,3,4))
