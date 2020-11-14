## Python元组&集合知识导航

> 1. 什么是元组？
> 2. 元组创建方式
> 3. 为什么要将元组设计成不可变序列
> 4. 元组遍历
> 6. 集合创建、增、删、改操作
> 7. 集合生成式

## 1	什么是元组？

> 列表，非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网 站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素， 元组可以满足这种需求。

不可变序列 & 可变序列

* 不可变序列：字符串、元组（没有增删改操作）
* 可变序列：列表、字典（可以对序列进行增删改操作，对象地址不发生改变）

## 2	元组定义

> 列表创建：`s = []`
>
> 元组创建：`s = ()`
>
> 字符串创建：`s = 'python'`（其中双引号或三引号都可以）
>
> 字典创建：`s = {}`

创建方式：

* 直接小括号：`t = ('python','Java',99)`
* 使用内置函数tuple()：`t = tuple(('python','Java',99))`
* 只含一个元祖的元素需要使用逗号和小括号：`t = (100,)`

```python
# 方式1
t = ('python', 'Java', 'C++', 99)
print(t)
print(type(t))

# 方式二使用内置函数
t1 = tuple(('python', 'Java', 'C++', 99))
print(t1)

t3 = ('aaa',)
print(t3)
```

运行结果：

```
('python', 'Java', 'C++', 99)
<class 'tuple'>
('python', 'Java', 'C++', 99)
('aaa',)
```

栗子：试图修改元组的一个元组，是否成功

```python
s = ('hell', 'world')
s[0] = ('hello',)
print(s)
```

试图修改第一个元素的值，导致Python返回类型错误消息。由于试图修改元组的 操作是被禁止的，因此Python指出不能给元组的元素赋值：

```python
Traceback (most recent call last):
  File "/Volumes/DATA/pythonProject/pythonProject1/python1/demo4.py", line 20, in <module>
    s[0] = ('hello',)
TypeError: 'tuple' object does not support item assignment
```

## 3	为什么要将元组设计成不可变序列

* 在多任务环境下，同时操作对象时不需要加锁

* 因此，在程序中尽量使用不可变序列

  > 注意事项：元组中存储的是对象的引用
  >
  > （1）如果元组中对象本身不可对象，则不能再引用其它对象
  >
  > （2）如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变

## 4	元组遍历

集合（底层使用hash）

* python语言提供内置数据结构
* 与列表、字典一样都属于可变类型的序列
* 集合是没有value的字典

```python
s = ('hell', 'world')
for i in s:
    print(i)
```



## 5	集合创建、增、删、改操作

（1）创建

* 直接 {}：s = {'pthon', 'Java'}
* 使用内置函数set()：s = set(range(6))

![image-20201005233932407](/Users/dimitri/Library/Application Support/typora-user-images/image-20201005233932407.png)

