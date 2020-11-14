# 公众号：MarkerJava
# 开发时间：2020/10/5 13:33

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
    print('对不起，你的成绩有误，请及时向老师反馈!')
