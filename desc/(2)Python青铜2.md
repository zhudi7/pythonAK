### 1、Print()函数

* 功能：向目的地输出内容
* 输出内容：数字、字符串、表达式
* 目的地：IDLE、控制台、文件

```python
# 可以输出字符串
print("hello")

# 可以含有运算符
print(3+3)

# 可以将数据输出文件
fg=open('/Users/dimitri/Desktop/python/text1.txt','a+')
print("aaa",file=fg)
fg.close()
```

### 2、转义字符

* 什么是转义字符？
  * 转义字符就是反斜+想要实现的转义功能首字母
* 为什么要转义字符？
  * 当字符串中包含反斜杆、单引号和双引号等有特殊用途的字符时，必须使用反斜杠对这些字符进行转义
  * 反斜杠：`\\`、单引号：`\'`、双引号：`\"`
  * 当字符串中包含换行、回车、水平制表符或者 退格等无法直接表示的特殊字符时，也可以使用转义字符。
  * 换行：`\n`、回车：`\r`、水平制表符：`\t`、退格：`\b`

效果如下

![](http://ww1.sinaimg.cn/large/006FuVcvgy1gj8sp888cuj30tx0jntax.jpg)

### 3、二进制与字符编码

以前有一个程序员爸爸，为了让计算机能够认识我，将我能够认识的字符和数字对应好，然后做成一张表叫ASCII表，告诉计算机某种符号你应该使用那个整数表示，'A'使用8个位（置）才能装得下我，在计算机中他们就是一个字节。

| 8bit(位)       | 1Byte(字节） |
| -------------- | ------------ |
| 1024Byte(字节) | 1KB          |
| 1024BK         | 1MB          |
| 1024MB         | 1GB          |

ASCII字符代码表

![](http://ww1.sinaimg.cn/large/006FuVcvgy1gj8tgm40rtj30dw0dnwnc.jpg)

### 4、python中的标志符与保留字

* 我的保留字
  * 有一些单词被我赋予了特定的意义，这些单词你在给你的任何对象起名字的时候都不能用
* 我的规则你必须要知道
  * 变量、函数、类、板块和其它对象的起名字就叫标识符
  * 规则：字母、数字、下划线；不能以字母开头；不能是我的保留字、严格区分大小

```python
import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 5、python中的变量与数据类型

变量的定义和使用

* 变量是内存中一个带标签的盒子

![image-20200930180405671](/Users/dimitri/Library/Application Support/typora-user-images/image-20200930180405671.png)

* 变量由三部分组成
  * 标识：表示对象所存储的内存地址，使用内置函数id(Obj)来获取
  * 类型：表示的是对象的数据类型，使用内置函数type(Obj)来获取
  * 值：表示对象所存储的具体数据，使用print(Obj)可以将值进行打印输出

* 数据类型
  * 整数类型：int——>98
  * 浮点数类型：float——>3.1415
  * 布尔类型：bool——>True,false
    * 用来表示真假的值
  * 字符串类型：str——>'人生苦短，我用python'
    * 字符串又称为不可变的字符序列
    * 可以应用单引号、双引号、三引号来定义
    * 单引号和双引号定义的字符串必须在一行
    * 三引号定义的字符串可以分在连续的多行
* 整数的不同进制表达式
  * 十进制：默认的进制
  * 二进制：以0b开头
  * 八进制：以0o开头
  * 十六进制：0x开头

### 6、数据类型转换

为什么要数据类型转换？

* 将不同的数据类型的数据并接在一起

```python
# 公众号：MarkerJava
# 开发时间：2020/10/4 17:27

name = '詹姆斯'
age = 20
print(type(name),type(age))
# print('我是'+name+'今年'+age)   #当将str类型与int类型进行连接时，报错解决方案，类型转换
print('我是'+name+'今年，'+str(age)+'岁')
```

### 7、input()函数的介绍

input函数

* 作用：接收来自用户的输入
* 返回值类型：输入值类型为str
* 值的存储：使用=对输入的值进行存储

```python
present = input('请输出你想要的礼物')
#变量 赋值运算符 input()函数是一个输出函数
```

栗子：

```python
present = input('请输出你想要的礼物：')
print(present,type(present))
```

![image-20201004191422966](/Users/dimitri/Library/Application Support/typora-user-images/image-20201004191422966.png)

### 8、Python中常见的运算符

![image-20201004191745033](/Users/dimitri/Library/Application Support/typora-user-images/image-20201004191745033.png)

* 算术运算符：

  * 标准算术运算符：加(+)、减(-)、乘(*)、除(/)、整除(//)

  * 取余运算符：%

  * 幂运算符：**

    以下是代码演示：

    ```python
    print(1+1)  # 等于2
    print(2-1)  # 等于1
    print(2*3)  # 等于6
    print(1/2)  # 等于0.5
    print(11//2)    # 等于5
    print(11%2) # 取余
    print(2**4) # 幂
    ```

* 赋值运算符

  * 执行顺序：右——>左

* 布尔运算符

  * and和：真真为真、1假全假
  * or或：一真为真、全假为假
  * Not非：
  * in：
  * Not in：

* 位运算符

  * 位与&：对应数位都是1，结果数位才是1，否则位0

  * 位或 | ：对应数位都是0，结果数位才是0，否则位1

  * 左移位运算符<<：高位益处舍弃，低位补0

  * 右移位运算符<<：低位益出舍弃，高位补0

    ```python
    # 公众号：MarkerJava
    # 开发时间：2020/10/4 23:32
print(4 << 1)   # 向左移动1位（移动一个位置）相当于乘以2
    print(4 << 4)   # 向左移动2位（移动两个位置）相当于乘以2的平方
    print(4 >> 1)  # 向右移动1位，相当于除以2
    print(4 >> 2)  # 向右移动2位，相当于除以2平方
    输出结果为：
    8
    64
    2
    1
    ```
    
    

### 9、python中的运算符的优先级

通常记住：算术第一、位于第二、比较第三、赋值为五