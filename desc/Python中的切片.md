## 切片

在 Python 里，像列表（list ）、元组（tuple ）和字符串（str ）这 类序列类型都支持切片操作，但是实际上切片操作比人们所想象的要强 大很多。首先我们来了解这些高级切片形式的用法。

为什么切片和区间会忽略最后一个元素?

在切片和区间操作里不包含区间范围的最后一个元素是 Python 的风 格，这个习惯符合 Python、C 和其他语言里以 0 作为起始下标的传统。 

对对象进行切片

用s = [a:b:c]的形式对 s 在 a 和 b 之间以 c 为间隔取值。c 的值还可以为负，负值意味着反向取值。栗子如下：

