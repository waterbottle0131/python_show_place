#面向对象基础与魔法方法
class ShoppingItem:
    def __init__(self,name,num,price):#__init__:初始化
        self.name=name
        self.num=num
        self.price=price

    def knock(self):
        print(f"已为您整理好购物清单信息：该商品的名称为:{self.name},购买数量为:{self.num}包,价格为:{self.price}元")


    def total(self,discount):
        total_money=self.price*self.num*discount/10
        print(f"您需要花费：{total_money:.1f}元")
        return total_money

    
    def __str__(self):#__str__:字符串表示方法
        return f"{self.name} {self.num} {self.price}"


    def __eq__(self, others):#__eq__:比较两个对象的内存地址是否相同
        return self.name==others.name and self.num==others.num and self.price==others.price

    
    def __lt__(self, others):#     __lt__:<      __le__:<=     __gt__:>     __ge__:>=
        return self.price<others.price

news_1=ShoppingItem("热巧克力奶",5,10)
news_1.knock()
news_1.total(8)

news_2=ShoppingItem("热巧克力奶",7,11)

print(news_1==news_2)
print(news_1<news_2)
