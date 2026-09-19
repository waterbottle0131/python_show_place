# #计算输入数字得出最大最小和平均数字的函数试探
# def function(a,b,c,d):
#     max_num=max(a,b,c,d)
#     min_num=min(a,b,c,d)
#     total=a+b+c+d
#     avg_num=total/4
#     print("最大值:",max_num,"最小值",min_num,"平均值",avg_num)
#     return{"max_num":max_num,"min_num":min_num,"avg_num":avg_num}
# print("请输入四个数,为您生成这四个数最大值,最小值,平均值")
# a=int(input("请输入第一个数:"))
# b=int(input("请输入第二个数:"))
# c=int(input("请输入第三个数:"))
# d=int(input("请输入第四个数:"))
# # function(a,b,c,d)


# lst=[]
# def function_b(*args):
#     max_num=max(args)
#     min_num=min(args)
#     avg_num=sum(args)/len(args)
#     print("最大值",max_num,"最小值",min_num,"平均值",avg_num)
#     return max_num,min_num,round(avg_num,1)

# i=int(input("请输入你要输入数字的个数:"))
# for s_index in range(i):
#     s=int(input(f"请输入第{s_index+1}个数字:"))
#     lst.append(s)
# print(lst)

# function_b(*lst)


def function_c(**kwargs):
    print(kwargs)

name=input("请输入名字:")
age=input("请输入年龄:")
area=input("请输入地区:")
gender=input("请输入性别:")
  

function_c(姓名=name,年龄=age,地区=area,性别=gender)
