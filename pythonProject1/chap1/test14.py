# 公众号：MarkerJava
# 开发时间：2020/10/5 15:02

# 要求从键盘输入密码，最多输入3次，如果正确结束循环
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，今天输入密码已经超过3次，请明天再次')

# for item in range(1,51):
#     if item % 5 != 0:
#         continue
#     print(item)
