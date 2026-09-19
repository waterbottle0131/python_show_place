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
