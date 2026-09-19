# #total_2=0
# #class_info=(
# #    ("李明",2026001,76),
# #    ("王浩",2026002,89),
# #    ("陈宇",2026003,94)
# #)
# print(class_info[1])
# print(class_info[2][2])
# print()
# print("姓名\t学号\t分数")
# for i in class_info:
#     print(f"{i[0]}\t{i[1]}\t{i[2]}")
#     total_2+=i[2]

# avg=total_2/3
# print(f"该班的总分是{total_2}，平均分是{avg:.1f}")

total=0
num=len(students)
students = (
    ("小赵",90),
    ("小钱",72),
    ("小孙",85),
    ("小李",58)
)

print("名字\t分数")
for name,score in students:
    print(f"{name}\t{score}")
    total+=score
    avg=total/num 
print(f"全班总分为{total},平均分为{avg:.1f}")    
lst=list(students)
lst.append(("小周",81))
tup=tuple(lst)
print(tup)
