# 公众号：MarkerJava
# 开发时间：2020/10/5 17:25

# 向列表的末尾添加一个元素
lst = [10,20,30,40,50,60,70,80]
# lst2 = ['hello','world']
# lst.append(lst2) # 这种方法将lst作为一个元素添加到列表的末尾
# lst.extend(lst2)
# print(lst)

# 任意位置添加
# lst.insert(1,111)
# print(lst)
# 在任意位置上添加N个元素
lst3 = ['python','Java']
lst[1:] = lst3
print(lst)

