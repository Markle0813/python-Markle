


# age = eval(input("请输入年龄"))
# if age >= 18 and age <= 60:
#     print("你好")
# else:
#     print("滚")


# has_ticket = True
# knife_long = 10
# if has_ticket:
#     print("检票成功")
#     print("欢迎乘车")
#     if knife_long > 20:
#         print("到太长了 %d 长" % knife_long)
#     else:
#         print("案件通过")
#
#
#
#
#
# else:
#     print("请买票")


# holiday_name = "平安夜"
# if holiday_name == "情人节":
#     print("买美国")
# elif holiday_name == "平安夜":
#     print("吃你妈")
# elif holiday_name == "傻逼节":
#     print("大哈比")
# else:
#     print("滚")


#


# python_score = 70
# if python_score >= 0 and python_score <= 60:
#     print("抱歉")
# else:
#     print("考试通过")


# is_yuangong = True
# if not is_yuangong:
#     print("禁止入内")
# else:
#     print("你好")


# age = 120
# if age >= 0 and age <= 100:
#     print("年龄正确")
# else:
#     print("年龄不争")


# age = 18
# if age >= 18:
#     print("欢迎进入网吧")
# else:
#     print("滚回去写作业")


# 第一次
# name_number = 114514
# print("我的学号是 %06d" % name_number)


# # 第二次演练
# price = 10.34
# weight = 20.52
# money = price * weight
# print("苹果单价 %.2f 重量为 %.2f 总金额为 %.2f" % (price,weight,money))
#
#
# #第三次演练
# scale = 0.25
# print("数据比例是 %.2f%% " % (scale * 100))


# age =eval(input("请输入年龄"))
# if age >= 60:
#     print("恭喜，你可以退休了")


# price = eval(input("输入单价"))
# weight = eval(input("输入重量"))
# money = price * weight
# print(money)


# import random
#
# player = eval(input("请输入 石头 1 剪刀 2 布 3"))
# computer = random.randint(1,3)
# print("玩家出拳的是 %d - 电脑出的拳是 %d "% (player, computer))
# if ((player == 1 and computer== 2)
#         or (player == 2 and computer == 3)
#         or (player == 3 and computer == 1)):
#
#      print("恭喜玩家获胜")
# elif (player == computer):
#      print("平手")
# else:
#      print("玩家输了")


#
# i = 0
# while i < 5:
#      print("Hello")
#      i += 1
# print("数字 %d" % i)


# result = 0
# i = 0
# while i <= 100:
#      print(i)
#      result += i
#      i += 1
# print("数字和 %d" % result)


# result = 0
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#         result += i
#     i += 1
# print("狮子王 %d" % result)


# result = 0
# i = 0
# while i <= 100:
#     if i % 2 != 0:
#         print(i)
#         result += i
#     i += 1
# print("狮子王 %d" % result)


# i = 0
# while i < 10:
#     if i == 3:
#         break
#     print(i)
#     i += 1


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#
#     print(i)
#     i += 1


# row = 1
# while row <= 5:
#     print("*" * row)
#     row += 1


# print("*",end= "")
# print("*")


# row = 1
# while row <= 9:
#     result = 1
#     while result <= row:
#         print("%d * %d = %d" %(row,result,row * result) ,end="    ")
#         result += 1
#     print("")
#     row += 1


# def sum_2num(num1,num2):
#     """"对两个数字地球和"""
#     # num1= 10
#     # num2 = 20
#
#     result = num1 + num2
#     print("%d + %d = %d" % (num1,num2,result))
# sum_2num(50,20)


# def sum_2_num(num1,num2):
#     """计算结果"""
#     result = num1 + num2
#     return result
# result_1 = sum_2_num(10,20)
# print("%d" % result_1)


# def text1():
#     print("$" * 50)
# def text2():
#     print("#" * 50)
#     text1()
#     print("*" * 50)
# text2()


# def print_line(char,times):
#     """打印次数"""
#     print(char * times)
# print_line("i",4)


# def print_line(char, times):
#     print(char * times)
#
#
# def print_lines(char, times):
#     rows = 0
#     while rows < 5:
#         print_line(char, times)
#         rows += 1
#
#
# print_lines("%", 50)









# name_list = ["zhangsan","lisi","wangwu"]
# print(name_list)
# name_list[0]
# name_list[1]
# name_list[2]
# ##必须为ipython





# # 定义列表
# name_list =["zhangsam","lisi","wangwu"]
#
#
#
# # 对应的数字
# print(name_list[2])
# print(name_list.index("wangwu"))
#
#
#
# # 更改对应变量
# name_list[1] = "李四"
# name_list[2] = "王五"
# name_list[0] = "张三"
#
#
# # 增加变量    append方法
# name_list.append("王小二")
# # insert方法 在指定变量后加入一个变量
# name_list.insert(1,"小美眉")
# # extend 增加一个列表
# temp1_list = ["孙悟空","猪二哥","沙师弟"]
# name_list.extend(temp1_list)
#
#
# # 删除
#
# # remove 删除指定元素
# name_list.remove("王五")
#
# # pop 默认删除最后一个变量
# name_list.pop()
# # pop 2 删除指定变量
# name_list.pop(2)
#
# # clear 清空所有列表
# name_list.clear()
#
#
#
# # 打印输出
# print(name_list)





# name_list = ["张三","李四","王五"]
# del name_list[1]
# # del删除列表元素 del从内存中删除 print将无法打印定义的变量 日常开发不建议使用del
# # 如下情况无法执行
# # name = "小米"
# # del name
# # print(name)
#
#
# print(name_list)






# name_list = ["张三","李四","王五","张三"]
# len_list = len(name_list)
# print("该变量中包含 %d 个元素" %len_list)
# # count 变量
# count = name_list.count("张三")
# print("张三出现了 %d 次" % count)
# # 删除扩展remove，只会删除第一次出现的数据
# name_list.remove("张三")
# print(name_list)


# name_list = ["zhangsan","lisi","wangwu","wangxiaoer"]
# num_list = [1,3,2,5,4]
# # 升序
# # name_list.sort()
# # num_list.sort()
#
#
#
# # 降序
# # name_list.sort(reverse=True)
# # num_list.sort(reverse=True)
#
#
#
#
#
# # 逆序
# name_list.reverse()
# num_list.reverse()
#
#
# print(name_list)
# print(num_list)




# name_list =["张三","李四","王五","王小二"]
# for my_name in name_list:
#     print("我的名字是 %s" % my_name)



# info_tuple = ("zhangsan",18,1.75)
# # print(info_tuple)
# info_tuple[0]
# info_tuple[1]
# info_tuple[2]
# # 用于ipython



# info_tuple = ("zhangsan",18,1.75)
# # 取字符串
# print(info_tuple[0])
# # 去索引
# print(info_tuple.index("zhangsan"))
# # 计数
# print(info_tuple.count("zhangsan"))
# # 统计
# print(len(info_tuple))



# info_tuple = ("zhangsan",18,1.75)
# for my_typle in info_tuple:
#     print(my_typle)


# info_tuple = ("小米",18,1.75)
# print("%s 年龄是 %d 身高是 %.2f " % info_tuple)
# tuple_str = "%s 年龄是 %d 身高是 %.2f " % info_tuple
# print(tuple_str)


# 转换
# hhh_list = [1,2,3,4]
# nihao_tuple = tuple(hhh_list)
# type(nihao_tuple)

# 字典
# xiaoming = {"name": "小明",
#             "age": 18,
#             "gender": True,
#             "height": 1.75,
#             "weight": 75.5}
# print(xiaoming)


# xiaoming = {"name": "小明"}
# # 取值
# print(xiaoming["name"])
# # 增加/修改
# xiaoming["age"] = 18
# xiaoming["name"] = "小小明"
# # 删除
# # xiaoming.pop("name")
#
#
#
#
#
#
# print(xiaoming)




# xiaoming = {"name": "小明",
#             "high": 1.75}
# # 统计
# print(len(xiaoming))
# # 增加字典
# tempw = {"age": 18,
#          "weight": 75.5}
# xiaoming.update(tempw)
# # 删除
# xiaoming.clear()
#
#
# print(xiaoming)


# xiaoming = {"name": "小明",
#             "qq": 12345,
#             "phone": 10086}
# for k in xiaoming:
#     print("%s - %s" % (k,xiaoming[k]))

# card_list = [
#     {"name": "张三",
#      "qq": 12345,
#      "phone": 110},
#     {"name": "李四",
#      "qq": 54321,
#      "phone": 10086}
# ]
# for card_info in card_list:
#     print(card_info)


# str1 = "hello world"
# str2 = '我的外号是"大西瓜"'
# print(str2)
# print(str1[6])
#
# for char in str2:
#     print(char)

# hello_ser = "hello hello"
# print(len(hello_ser))
#
# print(hello_ser.count("llo"))
# # print(hello_ser.count("abc"))
#
# print(hello_ser.index("llo"))


# space_str = "   "
# print(space_str.isspace())
# space_str = "    a"
# print(space_str.isspace())
# space_str = "    /t/n/r"
# print(space_str.isspace())

# num_str = "1"
# print(num_str)
# print(num_str.isnumeric())
# print(num_str.isdecimal())
# print(num_str.isdigit())
# num_str = "1.1"
# print(num_str)
# print(num_str.isnumeric())
# print(num_str.isdecimal())
# print(num_str.isdigit())


# hello_str = "hello world"
# print(hello_str.startswith("Hello"))
# print(hello_str.startswith("hello"))

# print(hello_str.endswith("llo"))

# print(hello_str.find("llo"))
# print(hello_str.find("abc"))


# print(hello_str.replace("hello","python"))
# print(hello_str)



# poem = ["woshi",
#         "yige",
#         "da",
#         "shabi"]
# for poem_str in poem:
#     # print("!%s!"% poem_str.center(10," "))
#     # print("!%s!" % poem_str.ljust(10, " "))
#     print("!%s!" % poem_str.rjust(10, " "))

# poem_str = "woshi\t yige\n\t dasha\t bi\n"
# print(poem_str)
#
# poem_list = poem_str.split()
# print(poem_list)
#
# result = " ".join(poem_list)
# print(result)


# num_str = "0123456789"
# print(num_str[0:3])
# print(num_str[:])
# print(num_str[5:])
# print(num_str[1::2])
# print(num_str[::2])
# print(num_str[-1])
# print(num_str[2:-1])
# print(num_str[-2:])
# print(num_str[-1::-1])

# a = [1,2,3]
# del a[1]
# print(a)
# del a
# # print(a)
# ser_str = "djfrfebfdjfjnfkefnjdn"
# max(ser_str)
# print(max(ser_str))
# min(ser_str)
# print(min(ser_str))



# [1,2,3,4,5,6,7,8,9][1:5]
# print([1,2,3,4,5,6,7,8,9][1:5])
# print((1,2,3,4,5,6,7,8,9)[1:5])


# print([1,2,3,4] * 5)
# print("hello"+"nihao")
# print((1,2)+(3,4))
# print([1,2]+[3,4])


# print("a" in "abcde")
# print("a" not in "abcde")




# for num in [1,2,3]:
#     if num == 2:
#         break
# else:
#     print("not run")
#     print(num)
# print(run)


# students = [
#     {"name":"阿土"},
#      {"name":"小明"}
# ]
# find_name = "阿土"
# for dirt_name in students:
#     print(dirt_name)
#     if dirt_name["name"] == find_name:
#         print("找到了 %s" % find_name)
#         break
# else:
#     print("没有找到 %s" % find_name)
# print("结束")


# a = 1
# id(a)
# print(id(a))
# b = a
# print(id(b))
# 下方变量不同
# a = 2
# print(id(a))
#
# def test(num):
#     print("对应函数值为 %d 对应 %d  " % num,id(num))
# a = 10
# print("a 对应的内存值为 %d " % id(a))
# test(a)
# result = "hello"
# print("地址 %d " % id(result))



# def demo():
#     demo = 10
#     print("函数内部变量为 %d" % demo)
# demo()
# def demo1():
#     pass
# demo()
# demo1()
# num = 10
# def demo1():
#     global num
#     num = 99
#     print("demo == %d" % num)
#
# def demo2():
#
#     print("demo == %d" %num)
# demo1()
# demo2()
# num = 10
# tittle = "你好"
# name = "小明"
# def demo():
#     print("%d" %num)
#     print("%s" %tittle)
#     print("%s" %name)
#
# demo()
def meantemp():
    print("测量中...")
    temp = 39
    weitness = 40
    print("测量结束...")
    return (temp,weitness)
result = meantemp()
print(result)













