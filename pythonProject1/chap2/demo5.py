# 公众号：MarkerJava
# 开发时间：2020/10/5 17:25

lst = [10,50,40,60,20,30,]
print('排序前列表:',lst)

lst.sort()
print('排序后列表:',lst)

# 通过指定关键字参数，将列表中元素进行降序排序
lst.sort(reverse=True)
print(lst)

lst2 = [7,5,6,4,2,3,1]
new_lst2 = sorted(lst2)
print(new_lst2)

# # 通过指定关键字参数，将列表中元素进行降序排序
desc_lst2 = sorted(lst2,reverse=True)
print(desc_lst2)