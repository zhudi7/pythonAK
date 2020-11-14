# 公众号：MarkerJava
# 开发时间：2020/10/5 17:25

# 列表创建方式一
lst = [10,20,30,40,50,60,70,80]
# 切片的结果-原列表片段的拷贝
# 切片的范围-[start,stop)左闭右开
print(lst[1:6:1]) # start=1,stop=6,step=1

# 省略step
print(lst[1:6]) # 默认step为1

# start=1,stop=6,step=2
print(lst[1:6:2])

# 省略start
print(lst[:6:2])

print('===判断指定元素是否在列表中====')
print(10 in lst) # 表示10在这个列表中存在吗？True
print(100 in lst) # 表示100在这个列表中存在吗？False
print(10 not in lst) # 表示10在列表中不存在，False
print(100 not in lst) # 表示100在列表中不存在，True

print('===遍历列表中元素====')
for item in lst:
    print(item)