# 公众号：MarkerJava
# 开发时间：2020/10/5 15:02

# 第一次取出来的是P，将P赋值item，将item的值输出
# for item in 'python':
#     print(item)

# range()产生一个整数系列，也是一个迭代对象
# for i in range(1,5,2):
#     print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为"—"
# for _ in range(3):
#     print('人生苦短，我用python')

# sum = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         sum += i
# print('sum=',sum)

# 要求输出100-999之间的水仙花数
for item in range(100,1000):
    ge = item % 10 # 个位
    shi = item // 10 % 10 # 十位
    bai = item // 100 # 百位
    # print(bai,shi,ge)
    if ge**3+shi**3+bai**3 == item:
        print(item)

