#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 字符串反转

"""
方式一
input_str = input("请输入：")
input_str_length = len(input_str)1
for i in range(input_str_length):
    print(input_str[input_str_length-i-1],end='')
"""
"""
方式二
input_str = input("请输入：")
print(input_str[-1::-1])
print(input_str[::-1])
"""

# 简易加法计算器  (5+5)=>10
"""
input_str = input("请输入加法表达式：")
new_input_str = input_str.strip()
new_input_list = new_input_str.split('+')
print(int(new_input_list[0]) + int(new_input_list[1]))
"""

# int类型转换 需要转换的数字中间可以存在空格
print(int(  3))
