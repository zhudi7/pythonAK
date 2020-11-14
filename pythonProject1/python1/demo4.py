# 公众号：MarkerJava
# 开发时间：2020/10/7 22:01

# 题目描述：给你一个字符串 a， 请你输出逆序之后的a

# names = ['张三', '李四', '王五']
# for item in names:
#     print('hello，'+item)
#     print("你的表演很精彩," + '\n')
# print('期待个位下次光临')

# 创建数值列表
# num = list(range(1, 11))
# print(num)
# 使用range函数，还可以指定步长，如需要打印（1-10）的偶数
# num1 = list(range(2,11,2)) # 函数range()从2开始数，然后不断地加2，直到达到或超过终值（11），
# print(num1)

def calc(a,b):
    c = a + b
    return c
result = calc(10,20)
print(result)
