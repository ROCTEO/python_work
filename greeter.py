#-*-coding:utf-8-*-
def greet_user(user_name):
    """显示简单的问候语"""
    print("Hello!"+user_name.title()+"!")

greet_user('zhang jin peng')

def display_message():
    """打印第八章的内容"""
    print("1、本章学习了定义函数\n2、创建时函数名括号的变量为形参\n3、调用时括号内的变量为实参")

display_message()

def favorite_book(title):
    """打印我最喜欢的书记"""
    print("One of my favorite book is "+title.title()+".")

favorite_book('alice in wonderland')
