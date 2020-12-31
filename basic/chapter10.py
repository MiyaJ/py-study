# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 16:11
# @Author  : Caixiaowei
# @File    : chapter10.py
# @Desc    : 函数和字符串的应用

import random
import string
from os.path import splitext

# 例子1：设计一个生成指定长度验证码的函数。
print('例子1：设计一个生成指定长度验证码的函数')
ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_code(code_len=4):
    code = ''
    for _ in range(0, code_len):
        index = random.randrange(0, len(ALL_CHARS))
        code += ALL_CHARS[index]
    return code


for _ in range(0, 3):
    print(generate_code())

# 例子2：设计一个函数返回给定文件名的后缀名。
print('例子2：设计一个函数返回给定文件名的后缀名')


def get_suffix(filename):
    split = filename.rfind('.')
    return filename[split + 1:] if split > 0 else ''


def get_suffix2(filename):
    arr = splitext(filename)
    return arr[1][1:]


print(get_suffix('abcd.txt'))
print(get_suffix('abcd.sql.md'))
print(get_suffix('.ignore'))

print(get_suffix2('abcd.txt'))