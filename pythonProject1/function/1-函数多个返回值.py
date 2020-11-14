# 公众号：MarkerJava
# 开发时间：2020/10/9 00:04

def test(a,b):
    x = a // b
    y = a % b
    #return [x, y] # 返回列表
    # return {'x':x, 'y': y} # 返回字典
    return (x, y) #返回元组
print(test(13,5))

def fun(n,b=''):
    return (n,b)
print(fun('hh'))
