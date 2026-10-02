#面向对象（定义类操作）---不推荐动态为对象添加属性
class Function:
    pass

c1=Function()
c1.name="小明"
c1.age=18
c1.gender="男"

print(c1.__dict__)

#推荐使用（__init__是初始化方法，对象创建后自动调用，self表示当前第一个创建的实例对象）
class Car:
    def __init__(self,c_name,c_age,c_gender):
        self.name=c_name
        self.age=c_age
        self.gender=c_gender
c1=Car("小明",18,"男")
print(c1.__dict__)
c2=Car("小红",17,"女")
print(c2.__dict__)