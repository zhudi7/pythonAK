# 公众号：MarkerJava
# 开发时间：2020/10/7 22:01

# 题目描述：给你一个列表 L, 对L进行升序排序并输出排序后的列表。
L = [8, 2, 50, 3]
for i in range(len(L)-1):
    for j in range(i, len(L)-1):
        if L[i] > L[j+1]:
            a = L[i]
            L[i] = L[j+1]
            L[j+1] = a
print(L)
