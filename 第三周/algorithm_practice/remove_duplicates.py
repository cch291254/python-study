
numbers=[3,1,3,2,1]

def remove_duplicates(numbers):
    data=[]
    seen=set()
    for number in numbers:
       
        if number not in seen:
            data.append(number)
            seen.add(number)
    return data
def count_numbers(numbers):
    counts={}
    for number in numbers:
        if number in counts:
            #counts[number]=counts.get(number,0)+1,简便写法
            counts[number]+=1
        else:
            counts[number]=1

    return counts
print(count_numbers([3, 1, 3, 2, 1]))
print(count_numbers([]))
print(count_numbers([5, 5, 5]))
result=remove_duplicates(numbers)
print(result)

#边界测试
print(remove_duplicates([]))
print(remove_duplicates([5,5,5]))
print(remove_duplicates([1,2,3]))
print(remove_duplicates([2,1,2,1,3]))

#测试是否修改原列表
print("去重结果：",result)
print("原列表：",numbers)


names=["Tom", "tom", "Alice", "ALICE", "Bob"]
def remove_duplicate_names(names):
    data=[]
    seen=set()
    for name in names:
        lower_name=name.lower()
        if lower_name not in seen:
            data.append(name)
            seen.add(lower_name)
    return data
print(remove_duplicate_names(names))
print(remove_duplicate_names([]))
print(remove_duplicate_names(["BOB","bob","Bob"]))  
