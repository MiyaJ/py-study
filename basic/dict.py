# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 13:53
# @Author  : Caixiaowei
# @File    : dict.py
# @Desc    : 字典, 类似Java中的 Map

# 申明: key 唯一, 后面的会覆盖前面的key-value
dict1 = {'key1': 'value1', 'you': '你', 'I': '我', 'he': '他', 'you': '你们'}
print(dict1)
print('you-:', dict1['you'])

# 内置函数
print('len:', len(dict1))
print('str:', str(dict1))
print('type:', type(dict1))

# 内置方法
# dict1.clear()
# print('clear:', dict1)

copy = dict1.copy()
print('copy:', copy)

keys = dict1.keys()
print('keys:', keys)
print('keys type', type(keys))

items = dict1.items()
print('type', items)
for i in items:
    print(i)
    print(type(i))
