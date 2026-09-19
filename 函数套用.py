# def add_function (x,y):
#     return x+y

# def pop_function (x,y):
#     return x-y

# def app_function (x,y,oper):
#     return oper(x,y)


# x=int(input("请输入x的值:"))
# y=int(input("请输入y的值:"))
# option=input("请选择调用函数的类型(1.add_function函数;2.pop_function函数):")
# if option=="1":
#    oper=add_function
# elif option=="2":
#    oper=pop_function
# else:
#    print("暂无该函数选项！")
# print(app_function(x,y,oper))

# a=lambda x,y:x*y
# x=int(input("请输入x的值:"))
# y=int(input("请输入y的值:"))
# print(a(x,y))



num_list = [17, 3, 92, 5, 28, 7, 41]
str_list = ["student", "campus", "activity", "research", "plan"]
data = [("张三", 19), ("李四", 21), ("王五", 18), ("赵六", 20)]
word_list = ["python", "sorted", "data", "campus", "star"]

#对列表内的数字进行从大到小排列
  #1.sort（）
num_list.sort(reverse=True)
print(num_list)
num_list.sort(key=lambda item:abs(item),reverse=True)
print(num_list)
  #2.sorted()
num_list_2=sorted(num_list,reverse=True)
print(num_list_2)

#对列表字符串内的字串进行按照长度来排
str_list_2=sorted(str_list,key=lambda item:len(item))
print(str_list_2)

#对列表内的元组进行数字高低来排
data.sort(key=lambda x:x[1],reverse=True)
print(data)
#对列表的字符串内的元素按照首字母来排
word_list_2=sorted(word_list)
print(word_list_2)