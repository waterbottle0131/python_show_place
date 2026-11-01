# 📋实验背景（统一给所有题目用）
# 某次心理学行为实验：
# 每位被试有多条试次(trial)
# 记录
# 一条记录包含：
# - subject_id：被试编号
#
# - trial_num：试次号
#
# - response：被试按键回答，字符串，值为  "OK"  或者  "NO" 
#
# - rt：反应时间（毫秒，数字）

#
# ✍️练习题目
#
# 题目1｜基础函数 +
# *args
#
# 要求：写一个函数  count_ok(*args) 
#
# - 参数 * args
# 可以传入多条response字符串（例如  "OK", "NO", "OK", "OK" ）
#
# - 功能：统计一共有多少个回答等于  "OK" ，返回数量
# 示例调用：count_ok("OK", "NO", "OK", "OK")
# # 预期输出：3
#
# def count_ok(*args):
#     n=0
#     for i in args:
#         if i=='OK':
#             n+=1
#     return n
# print(count_ok("OK", "NO", "OK", "OK"))
# 题目2｜ ** kwargs
# 接收单条被试记录
#
# 写函数  print_trial_info(**kwargs) 
#
# - 使用 ** kwargs接收一条试次的全部信息（subject_id, trial_num, response, rt）
#
# - 如果
# response == "OK"，就打印： "被试xxx，试次xx，选择OK，反应时：xxx ms" 
#
# 示例调用：print_trial_info(subject_id="S01", trial_num=2, response="OK", rt=456)
#
# def print_trial_info(**kwargs):
#     dict={}
#     for k,v in kwargs.items():
#         dict[k]=v
#     if dict.get("response")=="OK":
#         name=dict.get("subject_id")
#         times=dict.get("trial_num")
#         RT=dict.get("rt")
#         print(f"被试{name}，试次{times}，选择OK，反应时：{RT} ms")
#
# print_trial_info(subject_id="S01", trial_num=2, response="OK", rt=456)


#
# 题目3｜lambda + filter 筛选OK试次（非常适合实验数据）
#
#给定一个列表，里面存放多条response：
#
# resp_list = ["OK","NO","OK","NO","OK"]
#
#使用 filter() + lambda表达式，筛选出所有等于  "OK"  的元素，转为list打印出来
# resp_list = ["OK","NO","OK","NO","OK"]
# result=filter(lambda x: x=="OK",resp_list)
# ok_list=list(result)
# print(ok_list)
#
#              题目4｜文件IO：把所有OK试次写入txt文件
#
#              准备一个列表，里面是筛选好的OK试次字典：
#
#               ok_trials = [
#     {"sid":"S01","trial":1,"rt":520},
#     {"sid":"S02","trial":3,"rt":612}
# ]
#
#              编写代码，打开 / 创建  ok_result.txt ，把每一条OK试次信息写入文件，一行一条记录。
#
#              ✅加分：记得用try‑except捕获文件读写可能出现的异常

#
# ok_trials = [
#     {"sid": "S01", "trial": 1, "rt": 520},
#     {"sid": "S02", "trial": 3, "rt": 612}
# ]
#
# try:
#     with open("ok_result.txt", "w", encoding="utf-8") as f:
#         for trial in ok_trials:
#             line = f"被试:{trial['sid']},试次号:{trial['trial']},反应时rt:{trial['rt']} ms\n"
#             f.write(line)
#
#     with open("ok_result.txt", "r", encoding="utf-8") as f:
#         content = f.readlines()
#     print("文件读取结果：")
#     print(content)
#
# except Exception as e:
#     print(f"文件操作发生异常：{e}")

#
#              题目5｜简易面向对象：被试类 Subject，统计该被试OK数量
#
#              创建一个  Subject  类
#
#              1. 初始化函数接收：subject_id，以及该被试全部response列表
#
#              2. 写一个方法  get_ok_count() ，返回这个被试回答OK的总数
#              示例使用：s1 = Subject("S03", ["OK","NO","OK","OK"])
# # print(s1.get_ok_count()) #预期结果 3
# class Subject:
#     def __init__(self, subject_id,response):
#         self.subject_id = subject_id
#         self.response = response
#
#     def get_ok_count(self):
#         n=0
#         for i in self.response:
#             if i == "OK":
#                 n+=1
#         return f"被试编号:{self.subject_id},回答ok次数:{n}"
#
# s1 = Subject("S03", ["OK","NO","OK","OK"])
# print(s1.get_ok_count())


