# 公众号：MarkerJava
# 开发时间：2020/10/5 14:18

# 条件表达式
'''要求：从键盘录入两个整数，比较两个数的大小'''

num_a = int(input('请输入第1个数：'))
num_b = int(input('请输入第2个数：'))
# print('======常规写法======')
# if num_a >= num_b:
#     print(num_a,'大于等于',num_b)
# else:
#     print(num_a, '小于等于', num_b)

print('======使用表达式进行比较======')
print(str(num_a)+ '大于等于'+ str(num_b) if num_a >= num_b else str(num_a)+'小等于'+str(num_b))