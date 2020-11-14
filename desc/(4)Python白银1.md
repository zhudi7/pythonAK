## Python字符串知识导航

> 1. 字符串驻留的机制
> 2. 字符串查找操作
> 3. 字符串大小写转换操作
> 4. 字符串对齐和合并操作
> 5. 字符串劈分操作
> 6. 判断字符串
> 7. 字符串其它方法
> 8. 字符串比较
> 9. 字符串的切片操作
> 10. 格式化字符串
> 11. 字符串的编码转换
> 12. 总结

## 1	字符串驻留的机制

> 在python中字符串是基本数据类型，是一个不可变的字符序列。

（1）什么叫字符串驻留机制？

仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新的空间，而是把该字符串的地址赋给新创建的变量。

（2）如何创建字符串？

```python
# 字符串的三种创建方式
a = 'python'
b = "python"
c = '''python'''
# 输出字符串地址
print(id(a))
print(id(b))
print(id(c))
```

（3）字符串驻留机制优缺点

* 当需要值相同的字符串，可以直接从字符串池里面拿来使用，避免频繁的创建和销毁，提升效率和节约内存，因此拼接字符串和修改字符串是比较影响性能的。
* 在需要进行字符串拼接时建议使用srt类型的join方法，而非+，因为join()方法是先计算出所有字符串的长度，然后在拷贝，只new一次对象，效率比“+”效率高。

>列表创建：`s = []`
>
>元组创建：`s = ()`
>
>字符串创建：`s = 'python'`（其中双引号或三引号都可以）
>
>字典创建：`s = {}`

## 2	字符串查找操作

![image-20201006112758713](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006112758713.png)

## 3	字符串大小写转换操作

（1）upper()方法：将字符串所有字符都转换成大写字母

```python
a = 'Python,JAVA'
t = a.upper() # 转换成大写之后，会产生一个新的字符串对象
print(t)
```

运行结果：

```python
HELLO,WORLD,JAVA
```

（2）lower()方法：把字符串中所有字符都转换成小写字母。在存储数据时，很有用处，比如很多时候，你无法依靠用户来提供正确的大小写，因此 需要将字符串先转换为小写，再存储它们。

```python
name = 'hello,World,Java'
t = name.lower()
print(t)
```

运行结果：

```python
hello,world,java
```

（3）swapcase()方法：指把字符串中所有大写字母转换成小写字母，把所有小写字母都转成大写字母

```python
name = 'hello,World,Java'
t = name.swapcase()
print(t)
```

运行结果：

```python
HELLO,wORLD,jAVA
```

（4）capitalize()方法：把第一个字符串转换为大写，把其余字符串转换为小写

（5）title()方法：把第一个单词的第一个字符串转换为大写，把其余单词转换转换为小写。改方法很有用， 因为你经常需要将名字视为信息。例如，你可能希望程序将值Ada、ADA和ada视为同一个名字， 并将它们都显示为Ada。

![image-20201006112855763](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006112855763.png)

## 4	字符串对齐和合并操作

合并，Python使用加号（+）来合并字符串。栗如

```python
first_name = 'hallo'
last_name = 'world'
full_name = first_name + "," + last_name
print(full_name)
```

运行结果：

```python
hallo,world
```

![image-20201006113621530](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006113621530.png)

## 5	字符串劈分操作

![image-20201006113934361](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006113934361.png)

```python
a = 'Python|JAVA|C++'
print(a)
t1 = a.split(sep='|', maxsplit=1)
print(t1)

b = 'Python|JAVA|C++'
t2 = b.rsplit('|', maxsplit=1)
print(t2)
```

允许结果：

```python
Python|JAVA|C++
['Python', 'JAVA|C++']
['Python|JAVA', 'C++']
```

## 6	判断字符串

![image-20201006114722473](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006114722473.png)

## 7	字符串其它方法

![image-20201006114830344](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006114830344.png)

```python
# 字符串替换操作
a = 'Python,JAVA,C++，C++'
print(a.replace('Python', 'c++', 2))v #将python换成C++

# 字符串的合并操作
lst = ['python', 'java', 'c++', 'c']
pr = '|'.join(lst)
print(pr)
```

运行结果：

```python
c++,JAVA,C++，C++
python|java|c++|c
```



## 8	字符串比较

![image-20201006185914308](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006185914308.png)

## 9	字符串的切片操作

字符串是不可变类型

* 不具备增、删、改操作
* 切片操作时将产生新的对象

## 10	格式化字符串

格式化字符串的两种方式

* %作为占位符
  * %s：表示字符串
  * %i或%d：表示整数
  * %f：表示浮点数
* {}作为占位符



![image-20201006191643468](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006191643468.png)

格式化方式1:

```python
# 字符串格式化
name = '张三'
age = 20
print('我是%s,今年%d岁' % (name, age))
```

运行结果：

```python
我是张三,今年20岁
```

格式化方式二：

```python
# 字符串格式化
name = '张三'
age = 20
print('我叫{0},今年{1}岁'.format(name,age))
```

## 11	字符串的编码转换

编码与解码的方式

* 编码：将字符串转换为二进制数据（bytes）
* 解码：将bytes类型的数据转换成字符串类型

```python
# 字符串编码转换
s = "你好！"
print(s.encode(encoding='GBK')) # 一个中文占两个字节
print(s.encode(encoding='UTF-8')) # 一个中文占三个字节

# 字符串编码解码
# bytes代码一个二进制(字节类的数据）
bytes = s.encode(encoding='GBK')
print(bytes.decode(encoding='GBK'))

# UTF8
bytes = s.encode(encoding='UTF8')
print(bytes.deco
```

运行结果：

```python
b'\xc4\xe3\xba\xc3\xa3\xa1'
b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x81'
你好！
你好！
```

## 12	总结

![image-20201006193531274](/Users/dimitri/Library/Application Support/typora-user-images/image-20201006193531274.png)