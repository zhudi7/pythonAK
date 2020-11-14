## Python字典知识导航

> 1. 什么是字典
> 2. 字典的原理
> 3. 字典的创建
> 4. 字典的取值操作
> 5. Key判断与删除、新增操作
> 6. 字典获取视图操作
> 7. 字典元素的遍历
> 8. 字典的特点
> 9. 字典生成式

## 1	什么是字典

字典是python内置的数据结构之一，与列表一样是一个可变序列，以键值对的方式存储数据，字典是一个无序的序列。

## 2	字典的原理

字典的实现原理与查字典类似，查字典是先根据部首或拼音查找相应的页码，python中的字典是根据Key查找value所在的位置的。

## 3	字典的创建

字典创建方式

* 常用的方式：使用花括号`scores={'科比':100,'詹姆斯':99,'安东尼戴维斯':88}`
* 使用内置函数dict()：dict(name='kobe',age=20)

```python
scores = {'kobe': 100, 'lebron': 99, 'AD': 88}
print(scores)

sta = dict(name='lebron', age=36)
print(sta)
```

运行结果：

```python
{'kobe': 100, 'lebron': 99, 'AD': 88}
{'name': 'lebron', 'age': 36}
```

## 4	字典的取值操作

（1）`[]`取值与使用`get()`取值的区别

* `[]`如果字典中不存在指定的Key，抛出KeyError异常
* `get()`方法取值，如果字典不存在指定的Key，并不会抛出KeyError异常而是返回None，可以通过参数设置默认的value，以便指定的Key不存在时返回

```python
scores = {'kobe': 100, 'lebron': 99, 'AD': 88}
# 第一种方式使用[]
print(scores['kobe'])

# 第二种方式使用get()方法
print(scores.get('lebron'))
print(scores.get('ab'))
```

运行结果：

```
100
99
None
```

## 5	Key判断与删除、新增操作

（1）Key的判断

* in：指定的Key在字典存在返回true—>'kobe' in scores 
* Not int：指定Key在字典中不存在返回true—>'lebron' not in scores

```python
scores1 = {'kobe': 100, 'lebron': 99, 'AD': 88}
print('kobe' in scores1) # 判断kobe在字典中
print('kobe' not in scores1) # 判断kobe不在字典中

# 删除指定的key-value
del scores1['kobe']
print(scores1)

# 新增元素
scores1['张三'] = 66
print(scores1)

# 修改元素
scores1['张三'] = 67
print(scores1)
```

运行结果：

```python
True
False
{'lebron': 99, 'AD': 88}
{'lebron': 99, 'AD': 88, '张三': 66}
{'lebron': 99, 'AD': 88, '张三': 67}

```

## 6	字典获取视图操作

获取字典视图操作的三个方法：

* keys()——>获取字典中所有key
* value()——>获取字典中所有value
* items()——>获取字典中所有Key,value对

```python
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
```

运行结果：

```python
# 获取所有key
dict_keys(['kobe', 'lebron', 'AD'])
<class 'dict_keys'>
['kobe', 'lebron', 'AD']
# 获取所有的值
dict_values([100, 99, 88])
<class 'dict_values'>
# 获取所有键值对
dict_items([('kobe', 100), ('lebron', 99), ('AD', 88)])
<class 'dict_items'>
```

## 7	字典元素的遍历

```python
scores = {'kobe': 100, 'lebron': 99, 'AD': 88}

for item in scores:
    print(item, scores.get(item))
```

## 8	字典的特点

特点：

* 字典的所有元素都是一个Key-value对，Key允许重复，value可以重复
* 字典中元素是无序
* 字典的key必须是不可变对象
* 字典也可以根据需要动态地伸缩
* 字典会浪费较大的内存，是一种使用空格你就爱你换时间的数据结构

## 9	字典生成式

![image-20201005215024941](/Users/dimitri/Library/Application Support/typora-user-images/image-20201005215024941.png)

![image-20201005215043352](/Users/dimitri/Library/Application Support/typora-user-images/image-20201005215043352.png)

![image-20201005215152792](/Users/dimitri/Library/Application Support/typora-user-images/image-20201005215152792.png)

