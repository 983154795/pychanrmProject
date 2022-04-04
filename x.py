import math
import cmath
# print("{}是我们的计算机老师。".format("张三"))
# print("{0:6}的期末总分：{1:<9}".format("billy",621))
# print("{1}的成绩为{0}分".format(90,"李四"))
# print("{name}的成绩为{score}分".format(name="李四",score=90))
# print("{}的成绩为{}分。".format("李四",90))
#
# print("{0:.2f}".format(3.1415926))
#
# print("{0:6}的期末总分：{1:4}".format("billy",621))
# print("{0:>6}的期末总分为：{1:#>9}".format("sue",598))
# print("{0:^6}的期末总分为：{1:@^9}".format("sue",598))
# print("{0:<6}的期末总分为：{1:x<9}".format("sue",598))
# print("{}{}{}".format("小明","成绩为",90))
#
# x=input("请输入工资：")
# y=input("请输入奖金：")
# print("您的实发工资为：{}".format(eval('x+y')))

# ss="呼和浩特民族"
# print("{0:50}".format(ss))
# print("{0:>50}".format(ss))
# print("{0:*^50}".format(ss))
# print("{0:_^50}".format(ss))
# print("{0:5}".format(ss))
#
# n1=1234.5678
# n2=12345678
# print("{0:_^20,}".format(n2))
# print("{0:_^20}".format(n2))
# print("{0:_^20,}".format(n1))
# print("{0:.2f}".format(n1))
# print("{0:_^20.3f}".format(n2))
# print(ss)
# print("{0:.4}".format(ss))
#
# print("{0:b},{0:d},{0:o},{0:x},{0:X}".format(425))
# print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
# print("{0:.2e},{0:.2E},{0:.2f},{0:.2%}".format(3.14))
#
#
# print(abs(-3.7))#3.7
# print(chr(56))#A
# print(ord('0'))
# print(eval('1+1'))
# print(float('1'))
#

#
#
# print("math.fabs(-56.19):",math.fabs(-56.19))
# print("math.pow(2000,-4):",math.pow(2000,-4))
# print("math.sqrt(16):",math.sqrt(16))
# print("math.sin(math.pi):",math.sin(math.pi))
# print("math.radians(30):",math.radians(30))
# print("pi=",math.pi)
# print("e=",math.e)
# print()
# print("=================================================")
# print()
# import random
# print(random.choice([1,2,34,5,6,7]))
# print(random.random())
# print(random.randint(1,100))
# print(random.randrange(0, 100, 2))
# print(random.sample('abcdefg', 3))
# print(random.shuffle([1,4,9,16]))
# print(random.uniform(2,5))
# print()
# print("=================================================")
# print()
# x=input("请输入节日名称：")
# y=input("请输入收件人名称：")
# z=input("请输入送件人名称")
# print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")
# print("        节        日        祝        福")
# print("亲爱的：{}".format(y))
# print("             祝您 {0} 快乐！！".format(x))
# print("{0:>45}".format(z))
# print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")

#
# x=input("请输入一个符号")
# print("{0: ^5}".format(x))
# print("{0: ^5}".format(x*3))
# print("{0: ^5}".format(x*5))
#
#
#
# x,y,z = map(int,input("请输入三个整数a、b、c, 数与数之间以逗号分开：").split(","))
# if -10000<x<10000 and -10000<y<10000 and -10000<z<10000:
#     t= (x+y)*z
#     print("(x+y)*z的值为：{}".format(t))
# else:
#     print("输入值超出范围")
#
# y=int(a)//10%10
# z=int(a)//100%10
# print("倒序输出结果为：{}{}{}".format(x,y,z))
#
#
#
# a=input("请输入一个三位数的数字：")
# x=int(a)%10

# mark=eval(input("请输入成绩"))
# if 0<=mark<=100:
#     if mark<60:
#       result="合格"
#     elif mark<70:
#         result="及格"
#     elif mark < 80:
#         result = "中"
#     elif mark < 90:
#         result = "良"
#     else:
#         result = "优"
# else:
#     print("非法输入")
# print(result)
#
# grade=eval(input("请输入分数："))
# if grade>=60:
#     result="合格"
# else:
#     result = "淘汰"
# print(result)
#
# grade=eval(input("请输入分数："))
# result = "淘汰"
# if grade>=60:
#     result="合格"
# print(result)

# a,b,c=eval(input("请输入三个系数:"))
# if a==0:
#     print("不是")
# else:
#     delta=b*b-4*a*c
#     if delta==0:
#         print("有一个根x=",end="")
#         print(-b / 2 * a)
#     elif delta>0:
#         print("有两个根：\n x1=", end="")
#         print((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))
#         print("x2=", end="")
#         print((-b - math.sqrt(b * b - 4 * a * c)) / (2 * a))
#     else:
#         print("有不同的虚根")
#         print("此方程无实数根！")
# print()
# print("======================================================")
# print()
# import math
# a,b,c=eval(input("请输入三条边："))
# if a+b>c and b+c>a and a+c>b:
#   mark=0
#   if a==b or b==c or a==c:
#       mark=1
#       if a==b==c:
#           print("等边",end="")
#       else:
#           print("等腰",end="")
#   if math.fabs(a*a+b*b-c*c)<0.001 or math.fabs(b*b+c*c-a*a)<0.001 or math.fabs(a*a+c*c-b*b)<0.001:
#      mark=1
#      print("直角",end="")
#   if mark==0:
#       print("一般",end="")
# else:
#     print("不是",end="")
# print("三角形")
#
# a,b,c=eval(input("请输入三条边"))
# if a+b>c and b+c>a and a+c>b:
#     mark=0
#     if a==b or b==c or a==c:
#         mark = 1
#         if a==c==b:
#             print("是等边三角形")
#         elif math.fabs(a*a+b*b-c*c)<0.001 or math.fabs(b*b+c*c-a*a)<0.001 or math.fabs(a*a+c*c-b*b)<0.001:
#             print("是等腰直角三角形")
#         else:
#             print("是等腰三角形")
#     if (math.fabs(a*a+b*b-c*c)<0.001 or math.fabs(b*b+c*c-a*a)<0.001 or math.fabs(a*a+c*c-b*b)<0.001) and mark==0:
#         print("是直角三角形")
#         mark=2
#
#     if mark==0:
#         print("是一般三角形")
# else:
#     print("不是三角形")

# i=5
# while i>0:
#     i=i-1
#     print(i)

# s=0
# i=1
# while i<=100:
#     s=s+i
#     i=i+1
# print("1到100的和为：",s)
#
#
# s=0
# i=1
# while i<=100:
#     s=s+i
#     i=i+2
# print("1到100的所有奇数和为：",s)
#
# s=0
# i=2
# while i<=100:
#     s=s+i
#     i=i+2
# print("1到100的所有偶数和为：",s)
#
# for x in "ABCD":
#     print(x,end=" ")
# print()
#
# for x in range(6):
#     print(x,end=" ")
# print()
# for x in range(1,6):
#     print(x,end=" ")
# print()
#
# for x in range(1,6,2):
#     print(x,end=" ")
#
# city=['北京','上海','西安','成都','内蒙古']
# for x in range(len(city)):
#     print(x,city[x])
#
# # for x in print("e:\\x.txt"):
# #     print(x,end="")
#
# n=eval(input("请输入n值"))
# s=0
# for i in range(1,n+1):
#     s=s+pow(-1,i+1)*i
# print(s)

# t=[input("请输入所有学生的成绩")]
# s=0
# while i<len(t):
#     print(i)
#    # s=s+t[i]
#     i=i+1
# #print(s/len(t))
#
# numbers=[]
# while True:
#     x=input('请输入学生成绩，以回车为一个成绩的结尾，以n为录入的结尾：')
#     numbers.append(int(x))
#     while True:
#         flag="y"
#         if flag.lower()not in('y','n'):
#             print('只能输入yes或no')
#         else:
#             break
#     if flag.lower()=='n':
#             break
# print(sum(numbers)/len(numbers))

# n=[]
# while True:
#     x=input('请输入一个学生的成绩，若输入为n,则程序退出:')
#     if x.lower()=='n':
#         break
#     n.append(int(x))
# print("平均成绩为：",sum(n)/len(n))

# a=int(input("请输入学生数量"))
# b=1
# c=0
# for b in range(a):
#     d=float(input("请输入第{}个学生的成绩：".format(b)))
#     c=c+d
# print("平均成绩为：",c/a)

# n=0
# while True:
#     if n%2==1 and n%3==2 and n%5==4 and n%6==5 and n%7==0 and n!=119:
#         break
#     n=n+1
# print("第二个符合的台阶数为：",n)

# n=200
# while True:
#     if n%17==0:
#         break
#     n=n-1
# print("200以内能被3整除的最大整数为：",n)
#
# print()
#
# s=0
# i=0
# while i<=100:
#     i = i + 1
#     if i%2!=0:
#         continue
#     s=s+i
# print("1到100的所有偶数和为",s)

# for i in range(1,10):
#     print()
#     for j in range(1, i+1):
#         print("%d*%d=%d"%(j,i,j*i),end="\t")
# print()
# print()
# print("===============================================  =======================")
# print()
#
# for i in range(1,10):
#     for j in range (1,i):
#         print(end="\t\t")
#     for k in range(i,10):
#         print("%d*%d=%d"%(i,k,i*k),end="\t")
#     print("")

# flag=0
# n=eval(input("请输入一个数字"))
# for i in range(1,n):
#     if i%3==0 and i%5==0:
#         flag=1
#     if flag==1:
#         print("最小公倍数为",i)
#         break
# print()
# print("=====================================================================")
# print()
# x=0
# n=eval(input("请输入一个大于1的整数"))
# i=2
# for t in range(n,1,-1):
#     while(i<t-1):
#        if t%i==0:
#            break
#        i+=1
#     else:
#        print("最大素数为：",t)
#        break
#
# n=eval(input("请输入"))
# a=b=1
# print('%6d%6d'%(a,b),end="")
# count=2
# for i in range(3,n+1):
#     c=a+b
#     print('%6d'%c,end="")
#     count=count+1
#     if count%6==0:
#      print()
#     a=b
#     b=c
#
# print("=====================================================================")
# print("第一题:")
# for i in range(1,5):
#     print("{0: ^7}".format("*"*(2*i-1)))
# print()
# print("=====================================================================")
# print("第二题:")
# for i in range(1,5):
#     print("{0: ^7}".format("*"*(2*i-1)))
# for i in range(3,0,-1):
#     print("{0: ^7}".format("*"*(2*i-1)))
# print()
# print("=====================================================================")
# print("第三题:")
# print()
# for i in range(1,5):
#     print("{0: ^7}".format(chr(64+i)*(2*i-1)))
# print()
# print("=====================================================================")
# print("第四题:")
# print()
# for i in range(1,5):
#     print(" " * (4 - i), end="")
#     for j in range(65,64+2*i):
#         print(chr(j), end="")
#         # print("{0: ^7}".format(chr(j)),end="")
#     print()
# print()
# print("=====================================================================")
# print("第五题:")
# print()
# for i in range(1,5):
#     print(" " * (4 - i), end="")
#     for j in range(1,2*i):
#         if j%2==0:
#             print("+",end="")
#         else:
#             print("*", end="")
#     print()
# print()
# print("=====================================================================")
# print("第六题:")
# print()
# for i in range(1,5):
#     print(" " * (4 - i), end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     for j in range(i-1,0,-1):
#         print(j,end="")
#     print()
# print()
# print("=====================================================================")
# print("第七题:")
# print()
# for i in range(1,5):
#     print("{0: ^7}".format("中"*(2*i-1)))
# print()
# print("=====================================================================")
# print("第八题:")
# print()
# sum="呼和浩特"
# for i in range(1,len(sum)+1):
#     print(" " * (4 - i), end="")
#     print(sum[0:i])
#
# for i in range(1,5):
#     print(" " * (4 - i), end="")
#     for j in range(1,2*i):
#         print("中",end="")
#     print()

# L=['a','b','c','d','e','f']
# print(L[1:3])
#
# s=input("请输入多种水果名称（空格分开）：\n")
# a=reversed(list(s))
# print(a)

# print("=====================================================================")
# print("第一题：")
#
# x=input("请输入手机号：\n")
# y=x[3:7]
# z=x.replace(y,"****")
# print(z)
#
# print()
# print("=====================================================================")
# print("第二题：")
#
# x= input("请输入多种水果名称（空格分开）:\n")
# y = x.replace(" ", '\n')
# print(y)
# print()
# print("=====================================================================")
# print("第三题：")
#
# x=input("请输入一段话，系统将判断是否为回文：\n")
# y=x[::-1]
# if x==y:
#     print("此字符串是回文")
# else:
#     print("此字符串不是回文")

# L =[map(input("请输入多种水果名称（空格分开）").split())]
# print(L)
#
# x=input("请输入一段话，系统将判断是否为回文：")
# # print(len(x))
# # for i in range(1, len(x)):
# y=x[0:2]


#
# if list(a)==list(s):
#     print("是回文")
# else:
#     print("不是回文")

# a=[1,2,'3','4',5,'6']
# print(a)
# b=tuple(a)
# print(b)
# c=str(a)
# d=str(b)
# print(c,d)



print("=====================================================================")
print("第一题：")
x=input("请输入一个字符串：")
y=input("请输入想查找的字符：")
print(x,"中出现",x.count(y),"次",y)

print()
print("=====================================================================")
print("第二题：")
x2=input("请输入一个字符串：")
print("此字符串中，最大字符为：",max(x2),"，最小字符串为：",min(x2))

print()
print("=====================================================================")
print("第三题：")
str = input("请输入字符：")
print(str.swapcase())

print()
print("=====================================================================")
print("第四题：")
x3=input("请输入身份证号")
print(len(x3))
if len(x3)==18:
    print("身份证输入正确，您的生辰为：",x3[6:10],"年",x3[10:12],"月",x3[12:14],"日")
else:
    print("您输入的身份证号码有误，请核对后输入")

#获取一个随机数










































































































