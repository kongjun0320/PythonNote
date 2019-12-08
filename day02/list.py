#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 列表
# my_list = ['加油', '运动场', '图书馆', 777]
# len
# print(len(my_list))
# 索引
# print(my_list[1])
# 切片
# print(my_list[0: 2])
# for循环
# for item in my_list:
#     print(item)


# 练习1
"""
name_list = ["詹姆斯", "韦德", "罗斯"]
for item, index in enumerate(name_list):
    print(index, "===>", item)
"""

# append
"""
name_list = []
while True:
    input_str = input("请输入您的姓名：")
    name_list.append(input_str)
    print(name_list)
"""
# insert
"""
name_list = ["詹姆斯", "韦德", "罗斯"]
name_list.insert(1, "科比")
print(name_list)
"""

# remove pop  clear(清空)
"""
name_list = ["詹姆斯", "韦德", "罗斯"]
print(name_list.remove('韦德'))  # 返回None  入参是删除的内容
print(name_list.pop(0))  # 返回删除的元素  入参是要删除的索引
print(name_list)
"""
# del
"""
name_list = ["詹姆斯", "韦德", "罗斯"]
del name_list[1]
print(name_list)
"""

"""
    可变类型：list tuple
    不可变类型：int bool string
"""
print(type((1,2,3)))
