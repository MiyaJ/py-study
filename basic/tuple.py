# author    : Caixiaowei-zy
# date      : 2020/12/21 11:19
# description: 元组不可修改指的是--元组指向的内存中的内容不可变
tup1 = 1, 2, 3
tup2 = ('hello', 'tuple', '这是什么鬼', 3333)
print('申明tup1:', tup1)
print('申明tup2:', tup2)

# 取值
print(tup1[0])
print(tup2[1:7])

# 修改
# tup1[0] = 0
# print('修改后tup1:', tup1)

tup3 = tup1 + tup2
print('tup3:', tup3)

# 不能删除元组中的元素, 只能删除整个元组
# print(id(tup3))
# del tup3
# print('tup3 的id:', id(tup3))

# 索引
print('1是否在元组tup3中:', 1 in tup3)
print('1在tup3中的索引:', tup3.index(1))
print('tup3的长度:', len(tup3))
for i in tup3:
    print(i)