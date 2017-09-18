#_*_coding:utf-8_*_
class Dog():
    """创建一个dog类，模拟一只狗的行为"""
    def __init__(self,name,age):
        """定义本身属性"""
        self.name = name
        self.age = age

    def sit(self):
        """定义小狗坐下的指令"""
        print(self.name.title() + "is now  sitting.")

    def roll_over(self):
        """定义小狗翻滚的指令"""
        print(self.name.title() + "rolled over!")

mydog = Dog('wangcai',6)

print("My dog's name is " + mydog.name.title() +".")
