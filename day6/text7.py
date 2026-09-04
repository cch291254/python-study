names = ["张三", "李四", "王五", "赵六"]
scores = [85, 92, 78, 90]
max_n=""
max_s=0
for name,score in zip(names,scores):
    if score>max_s:
        max_n=name
        max_s=score
print(f"{max_n}:{max_s}")