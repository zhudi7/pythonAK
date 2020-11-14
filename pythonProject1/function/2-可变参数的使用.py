# 公众号：MarkerJava
# 开发时间：2020/10/9 00:01

nums = [1, 11, 7, 3, 5]


def test(item, *args):
    x = 0
    lst = []
    for i in item:
        x += i
        lst.append(i)
    lst.sort()
    print('最大值：%d' % lst[-1])
    print('最小值：%d' % lst[0])
    print('总和为：%d' % x)
    return x / 2


print('平均值：%d' % test(nums))
# print(test(([1, 3, 5]))) # 传元组
# print(test({5, 7, 9}))
