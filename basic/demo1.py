# author    : Caixiaowei-zy
# date      : 2020/12/16 16:49
from random import randint

""" 乘法表"""
for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + "*" + str(j) + '=' + str(j * i), end='\t')
        if i == j:
            print()
            break

''' 水仙花数 '''
list1 = []
for i in range(100, 1000):
    g = i % 10
    s = i // 10 % 10
    b = i // 100
    if i == g**3 + s**3 + b**3:
        list1.append(i)
print('水仙花数：', list1)
# i = int(987)
# print('个位：', i % 10)
# print('十位：', i // 10 % 10)
# print('百位：', i // 100)

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

''' 百钱百鸡 '''
for x in range(1, 21):
    for y in range(1, 34):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100 and z%3 == 0:
            print(x, y, z)

''' CRAPS赌博游戏 '''
money = int(1000)
while money > 0:
    print('你的资产为：', money)
    go_on = False
    while True:
        debt = int(input('请下注：'))
        if money > debt > 0:
            break
    # 第一次摇色子
    first = randint(1, 6) + randint(1, 6)
    print(f'\n玩家摇出了{first}点\n')
    if first == 7 or first == 11:
        print('玩家胜\n')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜\n')
        money -= debt
    else:
        go_on = True
    # 第一次摇色子没有胜负，继续
    while go_on:
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜\n')
            money -= debt
        elif current == first:
            print('玩家胜\n')
            money += debt
        else:
            go_on = True

print('输光了，游戏结束！')