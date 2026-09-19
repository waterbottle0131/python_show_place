import random
number=random.randint(1,100)
low=1
high=100

while True:
   a=int(input("请输入你所猜的数字(1,100):"))
   if a>number :
      print("这个数字太大了，再试试看")
      high=a-1
      print(f"已知数字范围为:{low},{high}")
   elif a<number:
      print("这个数字太小了，再试试看")
      low=a+1
      print(f"已知数字范围为:{low},{high}")
   else:
      print("恭喜，猜对了")
      break