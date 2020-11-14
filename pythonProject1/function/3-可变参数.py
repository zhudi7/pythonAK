# 公众号：MarkerJava
# 开发时间：2020/10/9 00:59

def test(a, b, *args):  # *ages表示可变参数
    print(a, b, args)


print(test(1, 2, 3, 4, 5, 5))  # 这就是可变参数，可以接收很多的参数


def add(a, b, *args, mu=1, **kwargs):   # **kwargs表示可变的关键字参数
    print('kwargs = {}'.format(kwargs))  # 多出来的参数会以字典的形式保存
    c = a + b
    for arg in args:
        c += arg
        return c * mu


print(add(1,2,3,4,5,mu=23,y = 4))