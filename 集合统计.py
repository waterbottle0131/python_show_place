data = [11, 22, 22, 33, 44, 44, 44, 55]
s1 = set(data)
print("s1去重之后：", s1)

#2.创建空集合，循环add添加元素
s2 = set()
num_list = [33, 44, 66, 77]
for n in num_list:
    s2.add(n)
print("s2添加完成：", s2)

#3.remove删除元素；in 判断元素是否存在
s2.remove(77)
print("s2删除77之后：", s2)
print("22是否在s1中：", 22 in s1)

#4.集合运算：交集、并集、差集
ji = s1 & s2   #交集，两边共同存在
bing = s1 | s2 #并集，全部去重
cha = s1 - s2  #差集：s1有，s2没有
print(f"交集：{ji}")
print(f"并集：{bing}")
print(f"差集 s1-s2：{cha}")

#5.for遍历集合，len统计集合元素数量
print("---遍历s1集合元素---")
for item in s1:
    print(item)
print(f"s1集合一共有 {len(s1)} 个元素")