# 公众号：MarkerJava
# 开发时间：2020/10/6 01:21

# 字符串编码转换
s = "你好！"
print(s.encode(encoding='GBK')) # 一个中文占两个字节
print(s.encode(encoding='UTF-8')) # 一个中文占三个字节

# 字符串编码解码
# bytes代码一个二进制(字节类的数据）
bytes = s.encode(encoding='GBK')
print(bytes.decode(encoding='GBK'))

# UTF8
bytes = s.encode(encoding='UTF8')
print(bytes.decode(encoding='UTF8'))