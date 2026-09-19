i=int(input("请输入你要输入到list_1的数字总个数:"))
list_1=[]
for i in range(1,i+1):
    import random
    number_1=random.randint(1,100)
    list_1.append(number_1)

j=int(input("请输入你要输入到list_2的数字总个数:"))
list_2=[]
for j in range(1,j+1):
    import random
    number_2=random.randint(1,100)
    list_2.append(number_2)

print("list_1为",list_1)
print("list_2为",list_2)

new_list=list_1+list_2

new_l_list=[]
for num in new_list:
    if num not in new_l_list:
        new_l_list.append(num)
print("去重后的列表为:",new_l_list)

# ====================== 列表 list [] ======================
# 列表：有序、可变，元素可以重复，支持增删改查
# 创建列表
#lst = [10, 20, 30, 20, 40]
#print("原始列表：", lst)

# 1. 索引取值，下标从0开始
#print("第0个元素：", lst[0])
#print("倒数第1个元素：", lst[-1])

# 2. 切片 [起始:结束:步长]，取左不取右
#print("切片 0~2：", lst[0:2])

# 3. 常用方法
#lst.append(50)      # 在末尾追加单个元素
#lst.insert(1, 15)   # 在索引1位置插入15
#lst.remove(20)      # 删除第一个值等于20的元素
#lst.pop()           # 默认删除最后一个元素，返回被删掉的值
#lst.pop(0)          # 删除指定下标元素
#lst[0] = 99         # 修改指定下标元素（列表可变，支持修改）
#print("修改后列表：", lst)

# 4. 内置函数
#print("列表长度len：", len(lst))
#print("最大值max：", max(lst))
#print("最小值min：", min(lst))

# 5. 查找统计
#print("20出现次数：", lst.count(20))
#print("20的索引位置：", lst.index(20))

# 6. 排序
#lst.sort()          # 原地从小到大排序
#lst.sort(reverse=True) # 原地降序
#lst.reverse()       # 原地反转列表

# 7. 列表推导式（高频，后面数据分析会用到）
#new_lst = [i*2 for i in range(1,6)]
#print("列表推导式结果：", new_lst)
