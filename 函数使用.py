
# def area(r):
#     area=3.14*r**2
#     return area
# a=int(input("请输入半径a为:"))
# c_area=area(a)
# print(c_area)


def circle(r):
    c=round(2*3.14*r,2)
    s=round(3.14*r**2,2)
    return c,s
r=float(input("请输入半径为:"))
p,a=circle(r)
print(f"圆的周长为{p},面积为{a}")