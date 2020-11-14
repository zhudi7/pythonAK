# 公众号：MarkerJava
# 开发时间：2020/10/5 17:25

# scores = {'kobe': 100, 'lebron': 99, 'AD': 88}
# 第一种方式使用[]
# print(scores['kobe'])

# 第二种方式使用get()方法
# print(scores.get('lebron'))
# print(scores.get('ab'))

scores1 = {'kobe': 100, 'lebron': 99, 'AD': 88}
print('kobe' in scores1)
print('kobe' not in scores1)

# 删除指定的key-value
del scores1['kobe']
print(scores1)

# 新增元素
scores1['张三'] = 66
print(scores1)

# 修改元素
scores1['张三'] = 67
print(scores1)
