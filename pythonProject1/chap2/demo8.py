# 公众号：MarkerJava
# 开发时间：2020/10/5 17:25

scores = {'kobe': 100, 'lebron': 99, 'AD': 88}
# 获取所有key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有key组成的视图转换层列表

# 获取所有的值
value = scores.values()
print(value)
print(type(value))  # 将所有value组成的视图转换层列表

# 获取所有键值对
items = scores.items()
print(items)
print(type(items))
