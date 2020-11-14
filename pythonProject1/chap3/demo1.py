# 公众号：MarkerJava
# 开发时间：2020/10/7 22:00

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fun(num):
    odd = [] # 存储奇数
    even = [] # 存储偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even
# 函数调用
print(fun(lst))
print("8888")
# 函数返回值：1，如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】return可以不写
