# 公众号：MarkerJava
# 开发时间：2020/10/5 17:25

sum = 0
for bai in range(1,5):
    for shi in range(1,5):
        for ge in range(1,5):
            if (bai != shi) and (bai != ge) and (shi != ge):
                sum += 1
                num = bai * 100 + shi * 10 + ge
                print(num, end=' | ')
    print()
print('总共为:', sum, '种方式')

sum1 = 0
for i in range(1, 5):
    for j in range(1, 5):
        for z in range(1, 5):
            if (i != j) and (i != z) and (j != z):
                sum1 += 1
                f = (i, j, z)
                print('%d%d%d' % f, end='|')
    print()
print('一共：%d种' % sum1)
