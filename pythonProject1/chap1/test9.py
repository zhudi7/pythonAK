# 公众号：MarkerJava
# 开发时间：2020/10/5 13:49

# 嵌套 if
'''题目要求：
    会员 >= 200 8zhe
        >= 100 9zhe
        不打折
    非会员 >= 200 9.5折
          <200 不打折
          '''

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
