#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 大小写转换
"""
my_str = 'my Name IS konGjun'
new_str1 = my_str.upper()
new_str2 = my_str.lower()
new_str3 = my_str.isnumeric()
print(new_str1)
print(new_str2)
print(new_str3)
"""

# isdigit() 和 isnumeric() 都是判断字符串是不是数字类型
"""
str_num = '0320'
print(str_num.isnumeric())
print(str_num.isdigit())
print("呵呵".isnumeric())
print(int(str_num))  # 320
"""

# 去空格
"""
my_str = ' ==  kong  jun  ==   '
print(my_str)
print(my_str.lstrip())
print(my_str.rstrip())
print(my_str.strip())
"""
# 字符串的替换
"""
print("我去你大爷的".replace('大爷',"**"))
"""
# 字符串切割
"""
print("2019-10-10".replace('-', '/'))
print("2019-10-10".split('-'))
"""
# 计算字符串的长度 包括字符串的前后空格
"""
print(len(' h eh '))
"""
# 字符串的索引
"""
my_str = 'kongjun'
print(my_str[1])
print(my_str[-1])
print(my_str[-3])
"""
# 切片
my_str = 'abcdefg'
# 起始位置从0开始 不包括终止索引
# print(my_str[1:4])
"""
字符串是有两套索引的
a  b  c  d  e  f  g
0  1  2  3  4  5  6  
-7 -6 -5 -4 -3 -2 -1
"""
print(my_str[0:3])
print(my_str[0:-4])
