# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 19:17
# @Author  : Caixiaowei
# @File    : chapter11.py
# @Desc    : 常用数据结构之列表
import random

# 1. 将一颗色子掷6000次，统计每个点数出现的次数
list1 = [0] * 6
for _ in range(6000):
    face = random.randint(1, 6)
    list1[face-1] += 1
print('1~6 一次出现的次数：', list1)

# 列表简单使用
list2 = ['hello', 'list', 333]
list3 = list('miya')
print('list2:', list2)
print('list3:', list3)

list4 = list2 + list3
print('list4:', list4)

print('hello' in list4)
print(list4[0])

print(list4[0: 3: 1])
print(list4[:])
