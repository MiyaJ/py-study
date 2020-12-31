# author    : Caixiaowei-zy
# date      : 2020/12/18 14:55
# 列表
# 1. 列表申明
list1 = [1, 2, 'hello', 'python', '天天', 'study', 3, 99]
list2 = list(list1)
print(list1)
print(list2)

size = len(list1)
print('list1 的大小为:', size)

list_0 = list1[0]
print('list1 索引0 的元素为:', list_0)

list1.append('小哥哥')
print(list1)

list1.append('小姐姐')
list1.insert(0, '小姐姐')
print(list1)

index = list1.index('小哥哥')
print(index)

# 切片
list3 = [00, 10, 20, 30, 40, 50, 60, 70, 60, 50, 50]
print('原列表:', list3)
print('原列表:', list3[1:])
print('切片后列表:', list3[1:6:1])
print('切片后列表:', list3[1:6:2])

print('步长 -1', list3[::-1])
print('步长 -1', list3[6:1:-1])

# 遍历
for i in list3:
    print('索引为:', list3.index(i), '元素值:', i)

# list3 中50 出现的次数
print('50出现的次数:', list3.count(50))

# 增加序列
list3.extend([1, 2, 3])
print(list3)

# 指定位置插入元素
list3.insert(0, '很忙啊')
print(list3)

# 移除指定位置的元素, 默认index=-1, 最后一个元素
list3.pop(0)
print(list3)

# 反向列表元素
list3.reverse()
print(list3)

# 排序
list3.sort()
print('排序:',list3)

# 复制
copy = list3.copy()
print('复制:', copy)

# 列表生成时
list4 = [2*i for i in range(1, 6)]
print(list4)
