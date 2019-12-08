#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    1、提示用户输入任意字符串
    2、计算用户输入字符串中数字的个数
"""

"""
while True:
    input_str = input("兄嘚，输入字符串呗...")
    intput_str_length = len((input_str))
    count = 0
    for i in range(intput_str_length):
        if input_str[i].isnumeric():
            count += 1
    print(count)
"""

# 取用户输入的最后两个值
my_input = input("请输入...")
input_length = len(my_input)
print(f"您输入的最后两个字符是：{my_input[input_length-2:]}")
print(f"您输入的最后两个字符是：{my_input[-2:]}")