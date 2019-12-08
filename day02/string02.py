#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 以**开头 以**结尾  可以判断以空格开始或者结束
"""
my_str = 'kongjun come on '
print(my_str.endswith(' '))
print(my_str.startswith('k o'))
"""
# encode  解释器读取到内存后 是用Unicode编码存储的 一个字符占4个字节
"""
name = '孔'
print(name.encode('utf-8'))  # 一个中文字符占三个字节
print(name.encode('gbk'))    # 一个中文字符占两个字节
"""

# join 把字符串中的每一个字符都用指定的字符串连接起来
"""
year_str = '20191010'
print(('-').join(year_str))
"""

# 字符串切片的步长  表示从开始索引加上步长再取  正负表示方向
my_str = "abcdefg"
"""
    abcdefg
    [-1:0:-1]
    表示 从-1取到0 默认步长为1 方向是从左向右
    这的步长是-1  表示 每次-1+(-1) 方向是从右向左
"""
print(my_str[-1:0:-1])
