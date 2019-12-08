# in 和 not in 的补充
# 判断字符或者字符串有没有在另一个字符串中出现 有则返回True 无则返回False
"""
my_str = '我爱我的祖国-中国'
print('中国' in my_str)  # True
print('中国人' in my_str)  # False
"""
# 练习：判断用户输入的内容是否包含铭感字符
"""
while True:
    input_str = input("请输入:")
    if input_str in '我是敏感字符':
        continue
    else:
        print(f"请输入的内容是{input_str}")
        break
"""
# 练习：用户的三次登录
"""
count = 0
while count < 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == 'kongjun' and password == '0320':
        print("登录成功!!")
        break
    else:
        count += 1
        if count == 3:
            print("账号被冻结了，请明天重试")
            break
        print("用户名/密码错误，请再次输入")
"""
# 练习：猜数字的游戏
import random

while True:
    input_num = int(input("来啊，你才啊..."))
    generate_num = random.randint(1, 5)
    if input_num == generate_num:
        print("哇，真厉害，猜对了")
        break
    else:
        print("很遗憾，猜错了，请继续")
