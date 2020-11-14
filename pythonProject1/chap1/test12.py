# 公众号：MarkerJava
# 开发时间：2020/10/5 15:02

# 要求：计算1-100之间偶数
sum = 0 # 用于存储累加
a = 1
while a <= 10:
    if not bool(a % 2):
        sum += a
    a += 1
print(sum)
