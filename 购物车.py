# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:PycharmProjects
# File_name:购物车.py
# Author: fan fan
# Time:2020年03月12日

'''
商品列表    ShangPinList
购物车列表  CarList
总资产  用户输入的  countMoney

显示商品列表的功能  printShangPin()

用户选择商品加入购物车功能 addCar()

用户购买功能 buy()

充值功能 addMoney()

从购物车移除功能 removeCar()
'''

class Car():
    def __init__(self,countMoney):
        #总资产
        self.countMoney = countMoney
        #商品列表
        self.shangPinList = [
            {'name':"电脑",'price':1999},
            {'name': "鼠标", 'price': 10},
            {'name': "游艇", 'price': 20},
            {'name': "美女", 'price': 998}
        ]
        #购物车列表
        self.carList = []

    #显示商品列表的功能
    def printShangPin(self):
        for j,i in enumerate(self.shangPinList):
            print(f"编号:{j} 商品名:{i['name']} 价格:{i['price']}")

    #用户选择商品加入购物车功能
    def addCar(self,id):
        self.carList.append(self.shangPinList[id])

    #用户购买功能
    def buy(self):
        countMoney = 0
        for i in self.carList:
            countMoney+=i['price']
        if self.countMoney >= countMoney:
            self.countMoney-=countMoney
            print(f"购买成功,余额为:{self.countMoney}")
        elif self.countMoney<countMoney:
            print("余额不足,请充值")

    #充值功能
    def addMoney(self,chongZhi):
        self.countMoney+=chongZhi

    #从购物车移除功能
    def removeCar(self,id):
        self.carList.pop(id)

    #查看购物车
    def showCar(self):
        for j,i in enumerate(self.carList):
            print(f"编号:{j} 商品名:{i['name']} 价格:{i['price']}")

    def show(self):
        print("="*30)
        print('1:打印商品列表')
        print('2:添加商品')
        print('3:购买商品')
        print('4:充值')
        print('5:移除商品')
        print('6:打印购物车列表')
        print('='*30)

    #run方法
    def run(self):
        while True:
            self.show()
            num = int(input("请输入功能编号:"))
            if num == 1:
                self.printShangPin()
            elif num == 2:
                id = int(input("请输入添加商品的编号:"))
                self.addCar(id)
            elif num == 3:
                self.buy()
            elif num == 4:
                chongZhi = int(input("请输入充值金额:"))
                self.addMoney(chongZhi)
            elif num == 5:
                id1 = int(input("请输入你要删除的商品编号:"))
                self.removeCar(id1)
            elif num == 6:
                self.showCar()

c = Car(2000)
c.run()