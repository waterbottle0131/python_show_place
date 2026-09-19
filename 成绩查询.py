#输入学生数量
count = int(input("学生人数："))
stu_list = []

#循环录入
for i in range(count):
    name = input("姓名：")
    id_num = input("学号：")
    yw = int(input("语文："))
    sx = int(input("数学："))
    yy = int(input("英语："))
    stu_list.append([name, id_num, yw, sx, yy])

#打印表头
print("姓名\t学号\t语文\t数学\t英语")
#循环输出每一个学生
for stu in stu_list:
    print(stu[0]+"\t"+stu[1]+"\t"+str(stu[2])+"\t"+str(stu[3])+"\t"+str(stu[4]))