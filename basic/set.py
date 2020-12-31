# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 14:36
# @Author  : Caixiaowei
# @File    : set.py
# @Desc    : 集合
set1 = set('abcdefgccc')
set2 = {1, 2, 'hello', 'world', 1, 'a'}
print(type(set1), set1)
print(set1)
print(set2)

print('diff:', set1.difference(set2))

i = iter(set2)
for x in i:
    print(x, end=' ')
