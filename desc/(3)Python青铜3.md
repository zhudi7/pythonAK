学完这篇文章你将掌握以下知识点

>1、程序的组织结构
>
>2、顺序结构
>
>3、对象布尔值
>
>4、选择结构
>
>5、分支结构（程序控制流程）
>
>6、pass空语句
>
>7、range()函数的使用
>
>8、while循环
>
>9、for-in循环
>
>10、break、continue与else语句
>
>11、嵌套循环

## 1、程序的组织结构

在1996年，计算机科学家证明了这样一个事实：任何简单或者复杂的算法都可以由**顺序结构、选择结构和循环结构**这三种基础结构组合而成。

## 2、顺序结构

顺序结构是指程序从上到下顺序执行代码，中间没有任何的判断和跳转，知道程序运行结束

## 3、对象布尔值

* python一切皆对象

  * 获取对象的布尔值：使用内置函数bool()

* 以下对象的布尔值为false

  * false

  * 数值()

  * None

  * 空字符串

  * 空元组

  * 空字典

  * 空集合

    ```python
    # 公众号：MarkerJava
    # 开发时间：2020/10/5 13:02
    print(bool(False))
    print(bool(0))
    print(bool(None))
    print(bool())
    print(bool([])) # 空列表
    print(bool(list())) # 列表
    print(bool(())) # 空元组
    print(bool(tuple())) # 空元组
    print(bool({})) # 空字典
    print(bool(dict())) # 空字典
    print(bool(set())) # 空集合
    ```

    

## 4、选择结构

程序根据判断条件布尔值选择性地执行部分代码。也就是明确让计算机知道什么条件下该执行怎么样的程序代码

## 5、分支结构（程序控制流程）

**单分支结构**：

```python
money = 1000 # 余额
s = int(input('请输入取款金额：')) # 取款金额
# 判断余额是否充足
if money >= s:
    money = money - s
    print('取款成功，余额为：',money)
```

**双分支结构**：

栗子：要求从键盘录入一个数，编写程序让计算机判断是奇偶数

```python
# 双分支
''' 从键盘录入一个数，编写程序让计算机判断是奇偶数 '''
num = int(input('请输出一个数：'))
# 条件判断
if num % 2 == 0:
    print(num,'是偶数')
else:
    print(num,'是奇数')

```

**多分支结构**：

语法结构：

```
if 条件表达式1:
条件执行体1
elif 条件表达式2
条件执行体2
elif 条件表达式N
条件执行体N
[elif:]
条件执行体N+1
```

栗子：要求从键盘录入一个整数成绩（90-100为优秀）、（80-89为良好）、（70-79为一般）、（60-69为及格）、（59以下为不及格）

```python
# 多分支
score = int(input('请输入成绩：'))
# 判断
if score >= 90 and score <= 100:
    print('成绩优秀，奖励一个棒棒糖')
elif score >= 80 and score <= 89:
    print('良好')
elif score >= 70 and score < 80:
    print('成绩一般')
elif score >= 60 and score < 70:
    print('成绩及格，请你多加努力!')
elif score >= 0 and score < 60:
    print('成绩不及格，是不是经常逃课，请及时弥补，下不为例')
else:
    print('对不起，成绩有误，请及时向老师反馈!')
```

**嵌套if**

栗子

```
题目要求：
    会员 >= 200 8zhe
        >= 100 9zhe
        不打折
    非会员 >= 200 9.5折
          <200 不打折
```

实现代码：

```python
answer = input('您是会员吗y/n？')
money = float(input('请输入您的购物金额：'))
if answer == 'y': # 会员
    print('会员')
    if money >= 200:
        print('打8折，付款金额为：',money * 0.8)
    elif 100 <= money <200:
        print('打9折，付款金额为：',money * 0.9)
    else:
        print('不打折，付款金额为：',money)
else:   # 非会员
    print('非会员')
    if money >= 200:
        print('非会员折后付款金额：',money * 0.95)
    else:
        print('不打折，付款金额为：',money)
```

**条件表达式**

栗子：要求从键盘录入两个整数，比较两个数的大小

```python
num_a = int(input('请输入第1个数：'))
num_b = int(input('请输入第2个数：'))
# print('======常规写法======')
# if num_a >= num_b:
#     print(num_a,'大于等于',num_b)
# else:
#     print(num_a, '小于等于', num_b)

print('======使用表达式进行比较======')
print(str(num_a)+ '大于等于'+ str(num_b) if num_a >= num_b else str(num_a)+'小等于'+str(num_b))
```

> 条件判断为true，则输入执行左边程序，否则相反。

## 6、pass空语句

* Pass语句：改语句什么都不做，只是一个占位符，用语法上需要语句的地方，起到作用就是让代码不报爆错
* 什么时候使用：先搭建语法结构，还没想好代码怎么写的时候
* 哪些语句一起使用？
  * if语句的条件执行体
  * for-in语句的循环体
  * 定义函数时的函数体

栗子：

```python
answer = input('您是会员吗y/n？')
money = float(input('请输入您的购物金额：'))
if answer == 'y': # 会员
    pass
else:   # 非会员
    pass
```

## 7、range()内置函数的使用

用于生成一个整数序列

三种创建range对象方式：

* range(stop)：创建一个[0，stop)之间的整数序列步长为1
* range(start, stop)：创建一个[start,stop]之间的整数序列，步长为为1
* range(start, stop,step)：创建一个[start，stop]之间的整数序列，步长为step

> 1. 返回值是一个迭代器对象

> 2. range类型的优点：不管range对象表示整数序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要存储start、stop、step，只有当用到range对象时，才会去计算序列中的相关元素

> 3. in与not in判断整数序列是否存在

栗子：

```python
s1 = range(5)
print(s1)
print(list(s1))

s2 = range(1,10)
print(s2)
print(list(s2))

s3 = range(1,10,2)
print(list(s3))

# 判断指定的整数是否在序列中in，not in
print(5 in s1) # 判断5在序列中
print(5 not in s1) # 判断5不在系列中

输出结果：
range(0, 5)
[0, 1, 2, 3, 4]
range(1, 10)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 3, 5, 7, 9]
False
True
```



## 8、while循环

反复做同一件事的情况称为循环

循环分类：while and for-in

语法结构：

```python
while 条件表达式
			条件执行体（循环体）
```

选择结构的if与循环while的区别

* if是判断一次，条件为true执行一次
* while是判断N+1次，条件为true执行N次

栗子1：

```python
# 公众号：MarkerJava
# 开发时间：2020/10/5 15:02

a = 1
b = 10
# 判断条件表达式
while a < b:
    print(a)
    a += 1
输出结果：
1
2
3
4
```

栗子2：要求计算0-5之间累加

```python
# 要求：计算0-5之间累加
sum = 0 # 用于存储累加
a = 1
while a <= 5:
    sum += a
    a += 1
print(sum)
运行结果：
15
```

栗子3：计算1-100的偶数和

```python
# 要求：计算1-100之间偶数
sum = 0 # 用于存储累加
a = 1
while a <= 100:
    if a % 2 == 0:
        sum += a
    a += 1
print(sum)

```

实现步骤：

* 初始化变量
* 条件判断
* 条件执行体（求和）

## 9、for-in循环

For-in循环

* in表达从（字符串、序列等）中依次取值，又称为遍历
* for-in遍历的对象必须是可迭代对象

for-in语法结构

```
for 自定义的变量 in 可迭代对象：
				循环体
```

栗子1：

```python
# 第一次取出来的是P，将P赋值item，将item的值输出
for item in 'python':
    print(item)

for i in range(1,10,2):
    print(i)
    
# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为"—"
for _ in range(3):
    print('人生苦短，我用python')
```

栗子2:要求使用for-in，求1-10之间的偶数和

```python
sum = 0
for i in range(1,11):
    if i % 2 == 0:
        sum += i
print('sum=',sum)
```

栗子3：要求输出100-999之间的水仙花数

```python
# 要求输出100-999之间的水仙花数
for item in range(100,1000):
    ge = item % 10 # 个位
    shi = item // 10 % 10 # 十位
    bai = item //100 # 百位
    # print(bai,shi,ge)
    if ge**3+shi**3+bai**3 == item:
        print(item)
```

## 10、break、continue与else语句

break语句：用于结束循环 结构，通常与分支结构if一起使用

栗子1：要求从键盘输入密码，最多输入3次，如果正确结束循环

```python
# 要求从键盘输入密码，最多输入3次，如果正确结束循环
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '888':
        print('密码正确')
        break
    else:
        print('
```

continue语句：用于结束当前循环，进入一次循环，通常与分支结构中的if一起使用

栗子2：要求输出1-50之间所有5的配数：5、10、15、、、

```python
for item in range(1,51):
    if item % 5 != 0:
        continue
    print(item)
```

else语句：与else语句配合使用的三种情况

```python
# 要求从键盘输入密码，最多输入3次，如果正确结束循环
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，今天输入密码已经超过3次，请明天再次')
```



## 11、嵌套循环

嵌套循环：循环结构中又嵌套另一个的完整的循环结构，其中内层循环作为外层循环的循环体执行

栗子1：9*9乘法

```python
# 9*9乘法
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i * j,end='\t')
    print(
```



栗子2：打印三角形

```python
# 输入直角三角形
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='')
    print()
```

![image-20201005163558416](/Users/dimitri/Library/Application Support/typora-user-images/image-20201005163558416.png)