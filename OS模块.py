# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:PycharmProjects
# File_name:OS模块.py
# Author: fan fan
# Time:2020年03月06日
'''
python自带的一个库
我们通过这个os模块可以来控制操作系统
'''
# 导入os模块
import os

'''文件的增删改查'''
#文件的增加:open("a.txt",'r')

#文件的删除:remove(r'文件的路径')
# os.remove(r"E:\bca1\a.txt")

#文件的更改:rename(r"源文件路径","目的文件路径")
# os.rename("stop.xls",r"f:\bca1\bca.xls")
# os.renames("a1.txt",r"f:\bca1\bca.xls")
#区别
#注意:这两个方法只能在当前模块所在的盘符下工作
#rename是重命名,目的路径如果没有的话,则报异常
#renames是重命名,目的路径如果没有的话,则创建

#文件的查询:listdir(路径)查询括号里路径下的文件或者文件夹以列表显示
# list = os.listdir(".")
# print(list)

'''文件夹的增删改查'''
#文件夹的增
#普通文件夹
# os.mkdir(r"b")
#递归文件夹
# os.makedirs(r"a\b\c\d")

#文件夹的删(前提：必须是空目录)
#删除递归目录和单个目录
# os.removedirs(r'a\b\c\d')
#删除单个空目录
# os.rmdir('a')

#文件夹的改
# os.rename(r'ccccc\a.txt','aaa')
# os.renames(r'ccccc\a.txt',r'a\b\c\a.txt')

#文件夹的查
# list = os.listdir('.')
# print(list)

'''os模块的常用命令'''
#获取当前所在位置
# pwd = os.getcwd()
# print(pwd)

#切换目录
# os.chdir(r"d:\aaa")
# pwd = os.getcwd()
# print(pwd)
# os.renames("c",r"d:\bca1\a")

#执行windows中cmd命令
# cmd = os.popen("calc")
# print(cmd.read())

#判断文件是否是一个普通文件,返回的是布尔值
# b = os.path.isfile("酒店.xls")
# print(b)

#判断文件是否是一个目录,返回的是布尔值
# d = os.path.isdir('酒店.xls')
# print(d)

#将路径与文件分隔开，返回是元组，注意：它不区分文件是否存在
# a = os.path.split(r"F:\PycharmProjects\untitled1\py_1910\demo04\aaaaa.txt")
# print(a)

#将文件后缀名与路径分隔开,返回的是元组,注意：它不区分文件是否存在
# a = os.path.splitext(r"F:\PycharmProjects\untitled1\py_1910\demo04\aaaa.txt")
# print(a)

#将盘符与路径分隔开，返回的是元组,注意：它不区分文件是否存在
# a = os.path.splitdrive(r"a:\PycharmProjects\untitled1\py_1910\demo04\aaaaa.txt")
# print(a)

#做一个查询文件的案例
'''
需求：
c:
    abc
        a
            a1.txt
            a1.jpg
        b
            b1.jpg
            b1.txt
        a.txt
        a.jpg
显示abc文件夹下的所有文件
c:\\abc
c:\\abc\\a
c:\\abc\\a\\a1.txt
c:\\abc\\a\\a1.jpg
...
'''