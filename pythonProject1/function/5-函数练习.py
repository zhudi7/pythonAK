# 公众号：MarkerJava
# 开发时间：2020/10/7 22:00


# 求[n,m)之间的整数之和
def test(n, m):
    x = 0
    for i in range(n, m):
        x += i
    return x / 2


result = test(0, 101)
print(result)


# 求n的介乘
def test1(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(test1(4))


# 计算m介乘的和
def test2(m):
    x = 0
    for i in range(0, m + 1):
        x += test1(i)
    return x


print(test2(5))
