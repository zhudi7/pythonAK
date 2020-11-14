# 公众号：MarkerJava
# 开发时间：2020/10/5 17:25

# 方式1
t = ('python', 'Java', 'C++', 99)
print(t)
print(type(t))

# 方式二使用内置函数
t1 = tuple(('python', 'Java', 'C++', 99))
print(t1)

t3 = ('aaa',)
print(t3)

# 空元组
t4 = ()
print(t4)

from pprint import PrettyPrinter