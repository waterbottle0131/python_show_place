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

## ====================== 元组 tuple () ======================
# 元组：有序、不可变，创建后不能新增、删除、修改元素；允许重复元素
# 适合存放固定不变的数据，安全，占用内存更小
# 创建元组举例
#tup = (10, 20, 30, 20, 40)
#print("原始元组：", tup)

# 1. 索引、切片（和列表一样，但是不能修改内容）
#print("下标0元素：", tup[0])
#print("切片0~3：", tup[0:3])

# 2. 内置函数
#print("元组长度len：", len(tup))
#print("最大值max：", max(tup))
#print("最小值min：", min(tup))

# 3. 查找统计
#print("20出现次数count：", tup.count(20))
#print("20的索引index：", tup.index(20))

# ⚠️重点：元组本身不可变！
# tup[0] = 99  这一行会直接报错，不能修改！

# 小知识点：元组里面如果嵌套列表，列表内部可以修改
#t2 = (1, [2,3])
#t2[1].append(4)
#print("嵌套列表的元组：", t2)

# 元组解包（非常常用）
#a,b,c = (100,200,300)
#print("解包：", a,b,c)
