# 公众号：MarkerJava
# 开发时间：2020/10/5 15:02

# for i in range(1,4):    # 行表，执三次，一次是一行
#     for j in range(1,5):
#         print('*',end='\t') # 不换行输出
#     print()

# 输入三角形
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# 9*9乘法
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i * j,end='\t')
    print()
