# 公众号：MarkerJava
# 开发时间：2020/9/30 16:23

# 可以输出字符串
print("hello")

# 可以含有运算符
print(3+3)

# 可以将数据输出文件
fg=open('/Users/dimitri/Desktop/python/text1.txt','a+')
print("aaa",file=fg)
fg.close()

import keyword
print(keyword.kwlist)
