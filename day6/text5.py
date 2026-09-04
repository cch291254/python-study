scores = [85, 59, 72, 45, 90, 58, 77]
sco_list=[f"{num}，{score}" for num,score in enumerate(scores) if score<60]
print(sco_list)