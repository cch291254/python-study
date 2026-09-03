students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}]
try1=[stu["name"] for stu in students if stu["score"]>80 ]
print(try1)


classes = {
    "一班": {"张三": 85, "李四": 92},
    "二班": {"王五": 78, "赵六": 95}}
try2=[f"{class_a}：{name}：{score_a}"
for class_a,stu1 in classes.items()
    for name,score_a in stu1.items()]
print(try2)
ist=text.split()
print(text_list)
word_count={word: text_list.count(word) for word in set(text_list)}
word_count1={}
word_count2={}
for word in text_list:
    if word in word_count1:
        word_count[word]+=1
    else:
        word_count1[word]=1
    word_count2[word]=word_count2.get(word,0)+1
print(word_count)
print(word_count1)
print(word_count2)
phone="13812345678"
masks=phone[:3]+"****"+phone[-4:]
print(masks)


text = "hello world hello python world hello"
text_l