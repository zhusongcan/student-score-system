# import re
# import json
#
# from rich import print
# from transformers import AutoTokenizer, AutoModel
#
# # 定义不同实体下的金融属性
# schema = {
#     '金融': ['日期', '股票名称', '开盘价', '收盘价', '成交量'],
# }
#
# # 信息抽取的模版
# IE_PATTERN = "{}\n提取上述句子中{}的实体，并按照JSON格式输出，上述句子中不存在的信息用['原文中未提及']来表示，多个值之间用','分隔。"
#
# # 提供一些例子供模型参考
# ie_examples = {
#     '金融': [
#         {
#             'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
#             'answers': {
#                 '日期': ['2023-01-10'],
#                 '股票名称': ['古哥-D[EOOE]美股'],
#                 '开盘价': ['100美元'],
#                 '收盘价': ['102美元'],
#                 '成交量': ['520000'],
#             }
#         }
#     ]
# }
# # 构建init_prompts()函数
# # 定义init_prompts函数
# def init_prompts():
#     """
#     初始化前置prompt，便于模型做 incontext learning
#     """
#     ie_pre_history = [
#         (
#             "现在你需要帮助我完成信息抽取任务，当我给你一个句子时，你需要帮我抽取出句子中实体信息，并按照JSON的格式输出，上述句子中没有的信息用['原文中未提及']来表示，多个值之间用','分隔。",
#             '好的，请输入您的句子。'
#         )
#     ]
#     for _type, example_list in ie_examples.items():
#         for example in example_list:
#             sentence = example["content"]
#             properties_str = ','.join(schema[_type])
#             schema_str_list = f'"{_type}"({properties_str})'
#             # print(schema_str_list)
#
#             # 填坑操作
#             sentence_with_prompt = IE_PATTERN.format(sentence, schema_str_list)
#             # print(sentence_with_prompt)
#             ie_pre_history.append((f"{sentence_with_prompt}", f"{json.dumps(example['answers'], ensure_ascii=False)}"))
#             # ie_pre_history.append((f"{sentence_with_prompt}", f"{json.jumps(example['answers'], ensure_ascii=False)}"))
#             print(ie_pre_history)
#             return ie_pre_history
# def inference(sentences:list, custom_settings:dict):
#     print(sentences, custom_settings)
#
# # if __name__ == '__main__':
# #     init_prompts()
# if __name__ == '__main__':
#     # device = 'cuda:0'
#     device = 'cpu'
#     # 预训练模型的分词器
#     tokenizer = AutoTokenizer.from_pretrained("/Users/ligang/PycharmProjects/llm/ChatGLM-6B/THUDM/chatglm-6b-int4",
#                                               trust_remote_code=True)
#     # model = AutoModel.from_pretrained("./ChatGLM-6B/THUDM/chatglm-6b",
#     # trust_remote_code=True).half().cuda()
#     # 预训练模型
#     model = AutoModel.from_pretrained("/Users/ligang/PycharmProjects/llm/ChatGLM-6B/THUDM/chatglm-6b-int4",
#                                       trust_remote_code=True).float()
#     model.to(device)
#
#     # 模型根据提示词训练完毕之后，对sentences的内容进行剥离
#     sentences = [
#         '2023-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
#         '2023-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。',
#     ]
#
#     custom_settings = init_prompts()
#
#     inference(sentences, custom_settings)
# print("欢迎使用教务系统")
# print("""##################"
# #      1.增加学生成绩
# #      2.查询学生成绩
# #      3.统计学生成绩
# #      4.退出教务系统
# ###################"""
#       )
# stu_message={}
# while True:
#     choice=int(input("请输入要执行的操作"))
#     match choice:
#         case 1:
#             stu_name=input("学生姓名")
#             stu_ch=int(input("语文成绩:"))
#             stu_ma=int(input("数学成绩:"))
#             stu_en=int(input("英语成绩:"))
#             if stu_name in stu_message:
#                 print("该学生已存在")
#             else:
#                 stu_message[stu_name]=[stu_ch,stu_ma,stu_en]
#         case 2:
#             stu_name = input("学生姓名")
#             if stu_name not in stu_message:
#                 print("该学生不存在")
#                 continue
#             else:
#                 stu_info=stu_message[stu_name]
#                 print(f"学生姓名{stu_name},语文成绩:{stu_info[0]},数学成绩:{stu_info[1]},英语成绩:{stu_info[2]}")
#         case 3:
#             stu_name = input("学生姓名")
#             if stu_name not in stu_message:
#                 print("该学生不存在")
#                 continue
#             score_ch=[]
#             score_ma=[]
#             score_en=[]
#             for name,score in stu_message.items():
#                 score_ch.append(score[0])
#                 score_ma.append(score[1])
#                 score_en.append(score[2])
#             ch_max,ch_min=max(score_ch),min(score_ch)
#             ma_max,ma_min=max(score_ma),min(score_ma)
#             en_max,en_min=max(score_en),min(score_en)
#             ch_avg=sum(score_ch)/len(score_ch)
#             ma_avg=sum(score_ma)/len(score_ma)
#             en_avg=sum(score_en)/len(score_en)
#             ch_max_stu=(name for name,score in stu_message.items() if score[0]==ch_max)
#             ch_min_stu=(name for name,score in stu_message.items() if score[0]==ch_min)
#             ma_max_stu=(name for name,score in stu_message.items() if score[1]==ma_max)
#             ma_min_stu=(name for name,score in stu_message.items() if score[1]==ma_min)
#             en_max_stu=(name for name,score in stu_message.items() if score[2]==en_max)
#             en_min_stu=(name for name,score in stu_message.items() if score[2]==en_min)
#             print("=" * 40)
#             print(f"语文最高分: {ch_max} 分，学生: {'、'.join(ch_max_stu)}")
#             print(f"语文最低分: {ch_min} 分，学生: {'、'.join(ch_min_stu)}")
#             print(f"语文平均分: {ch_avg:.2f} 分")
#             print("-" * 40)
#             print(f"数学最高分: {ma_max} 分，学生: {'、'.join(ma_max_stu)}")
#             print(f"数学最低分: {ma_min} 分，学生: {'、'.join(ma_min_stu)}")
#             print(f"数学平均分: {ma_avg:.2f} 分")
#             print("-" * 40)
#             print(f"英语最高分: {en_max} 分，学生: {'、'.join(en_max_stu)}")
#             print(f"英语最低分: {en_min} 分，学生: {'、'.join(en_min_stu)}")
#             print(f"英语平均分: {en_avg:.2f} 分")
#             print("=" * 40)
#         case 4:
#             print("感谢使用")
#             break
#         case _:
#             print("输入错误")
# money=5000000
# name=input("请输入你的姓名")
# while True:
#     choice=int(input("请输入要执行的操作"))
#     match choice:
#         case 1:
#             print(f"当前余额为{money}")
#         case 2:
#             add_sum=int(input("请输入你要存入的金额"))
#             money+=add_sum
#             print(f"余额为{money}")
#         case 3:
#             del_sum = int(input("请输入你要取出的金额"))
#             money -=del_sum
#             print(f"余额为{money}")
#         case 4:
#             print("感谢使用")
#             break
#         case _:
#             print("输入错误")
# file = open('致橡树', 'r', encoding='utf-8')
# print(file.read())
# file.close()
# file = open('致橡树', 'a', encoding='utf-8')
# file.write('\n标题：《致橡树》')
# file.write('\n作者：舒婷')
# file.write('\n时间：1977年3月')
# file.close()
# def text_a(computer):
#     result=computer(2,3)
#     print(result)
# def computer(x,y):
#     return x+y
# text_a(computer)
# try:
#     # 1/0
#     print(name)
# except NameError as e:
#     print("变量未定义")
# except ZeroDivisionError as z:
#     print("除0异常")
# import time
# print("你好")
# for i in range(1,6):
#     time.sleep(1)
#     print(i)
# print("我好")
# import my_utils.str_util
# print(my_utils.str_util.str_reverse("abcdefghijklmn"))
# 1. 添加学生成绩
# def add_student(score_data, name, score):
#     """
#     添加学生成绩
#     :param score_data: dict 存储所有学生成绩的字典
#     :param name: str 学生姓名
#     :param score: int 分数
#     :return: tuple (bool, str) 成功/失败状态 + 提示信息
#     """
#     if name in score_data:
#         return False,"学生已存在"
#     elif score<0 or score>100:
#         return False,"分数错误,应在0-100之间"
#     else:
#         score_data[name]=score
#         return True,"添加成功"
#
#     # 你的代码：
#     # 1. 判断姓名是否已存在，已存在则返回失败
#     # 2. 判断分数是否在0-100之间，不合法则返回失败
#     # 3. 添加到字典，返回成功提示
#
#
# # 2. 删除学生
# def delete_student(score_data, name):
#     """
#     删除指定学生
#     :param score_data: dict 成绩字典
#     :param name: str 学生姓名
#     :return: tuple (bool, str)
#     """
#     if name not in score_data:
#         return False,"学生不存在"
#     else:
#         del score_data[name]
#         return True,"删除成功"
#     # 你的代码：判断学生是否存在，存在则删除，不存在返回失败
#
#
# # 3. 查询成绩
# def query_score(score_data, name):
#     """
#     查询学生分数
#     :param score_data: dict 成绩字典
#     :param name: str 学生姓名
#     :return: tuple (bool, str)
#     """
#     if name not in score_data:
#         return False,"学生不存在"
#     else:
#         return True,f"学生{name}分数为{score_data[name]}"
#     # 你的代码：存在则返回分数，不存在返回失败提示
#
#
# # 4. 修改成绩
# def update_score(score_data, name, new_score):
#     """
#     修改学生分数
#     :param score_data: dict 成绩字典
#     :param name: str 学生姓名
#     :param new_score: int 新分数
#     :return: tuple (bool, str)
#     """
#     if name not in score_data:
#         return False,"学生不存在"
#     else:
#         score_data[name]=new_score
#         return True,"修改成功"
#     # 你的代码：判断学生是否存在、新分数是否合法，修改后返回结果
#
#
# # 5. 成绩统计
# def calc_stats(score_data):
#     """
#     统计全班成绩：人数、平均分、最高分、最低分
#     :param score_data: dict 成绩字典
#     :return: tuple (bool, dict/str) 成功返回统计结果字典，失败返回错误信息
#     """
#     if not score_data:
#         return False,"未找到学生"
#     else:
#         scores=list(score_data.values())
#         num=len(scores)
#         total=sum(scores)
#         avg=total/num
#         max_score=max(scores)
#         min_score=min(scores)
#         result={
#             "人数":num,
#             "平均分":avg,
#             "最高分":max_score,
#             "最低分":min_score
#         }
#         return True,result
#
# def main():
#     # 数据只在主函数中维护，不设全局变量
#     score_data = {}
#     while True:
#         print("\n=== 学生成绩管理系统 ===")
#         print("1. 添加学生成绩")
#         print("2. 删除学生")
#         print("3. 查询成绩")
#         print("4. 修改成绩")
#         print("5. 成绩统计")
#         print("6. 退出系统")
#         choice = input("请输入选项(1-6)：")
#         if choice == "1":
#             name = input("请输入学生姓名：")
#             score = int(input("请输入分数："))
#             a=add_student(score_data,name,score)
#             print(a)
#             # 补充：转成整数，调用add_student，打印返回的提示信息
#         elif choice == "2":
#             name=input("请输入学生姓名:")
#             a=delete_student(score_data,name)
#             print(a)
#             # 补充删除逻辑
#         elif choice == "3":
#             name = input("请输入学生姓名:")
#             a=query_score(score_data,name)
#             print(a)
#             # 补充查询逻辑
#         elif choice == "4":
#             name = input("请输入学生姓名:")
#             new_score=int(input("请输入学生的新分数"))
#             a=update_score(score_data,name,new_score)
#             print(a)
#             # 补充修改逻辑
#         elif choice == "5":
#             a=calc_stats(score_data)
#             print(a)
#             # 补充统计逻辑，格式化输出统计结果
#         elif choice == "6":
#             print("感谢使用，退出系统")
#             break
#         else:
#             print("输入无效，请输入1-6的数字")
# if __name__ == "__main__":
#     main()
#     # 你的代码：空数据返回失败；有数据则计算各项指标，返回统计字典
# import json
# data={"中国":"1","美国":"2","俄罗斯":"3"}
# json_str=json.dumps(data,ensure_ascii=False)
# print(type(json_str))
# print(json_str)
# s=json.loads(json_str)
# print(type(s))
# print(s)
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts
# line=Line()
# line.add_xaxis(["中国","美国","英国","俄罗斯","日本"])
# line.add_yaxis("GDP",[30,20,20,25,10])
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="90%")
# )
# line.render()
# from pyecharts.charts import Bar,Timeline
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
# # bar1=Bar()
# # bar1.add_xaxis(["中国","美国","日本"])
# # bar1.add_yaxis("GDP",[20,30,10],label_opts=LabelOpts(position="right"))
# # bar1.reversal_axis()
# # # bar1.render()
# # bar2=Bar()
# # bar2.add_xaxis(["中国","美国","日本"])
# # bar2.add_yaxis("GDP",[40,50,20],label_opts=LabelOpts(position="right"))
# # bar2.reversal_axis()
# # # bar2.render()
# # bar3=Bar()
# # bar3.add_xaxis(["中国","美国","日本"])
# # bar3.add_yaxis("GDP",[90,70,50],label_opts=LabelOpts(position="right"))
# # bar3.reversal_axis()
# # # bar3.render()
# # timeline=Timeline()
# # timeline.add(bar1,"点1")
# # timeline.add(bar2,"点2")
# # timeline.add(bar3,"点3")
# # timeline.add_schema(
# #     play_interval=1000,
# #     is_timeline_show=True,
# #     is_auto_play=True,
# #     is_loop_play=True
# # )
# # timeline.render()
# f=open("D/资料","r",encoding="GB2312")
# data_lines=f.readlines()
# f.close()
# data_lines.pop(0)
# data_dict={}
# for line in data_lines:
#     year=int(line.split(",")[0])
#     country=line.split(",")[1]
#     gdp=float(line.split(",")[2])
#     try:
#         data_dict[year].append([country,gdp])
#     except KeyError:
#         data_dict[year]=[]
#         data_dict[year].append([country, gdp])
# timeline=Timeline({"theme":ThemeType.LIGHT})
# sorted_year_list=sorted(data_dict.keys[])
# for year in sorted_year_list:
#     data_dict[year].sort(key=lambda x:x[1],reverse=True)
#     year_data=data_dict[year][0:8]
#     x_data=[]
#     y_data=[]
#     for country_gdp in year_data:
#         x_data.append(country_gdp[0])
#         y_data.append(country_gdp[1]/100000000)
#     bar=Bar()
#     x_data.reverse()
#     y_data.reverse()
#     bar.add_xaxis(x_data)
#     bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
#     bar.reversal_axis()
#     bar.set_global_opts(
#         title_opts=TitleOpts(title=f"{year}年份全球前八GDP数据")
#     )
#     timeline.add(bar,str(year))
# timeline.add_schema(
#     play_interval=1000,
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=False,
# )
# class student:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
# for _ in range(10):
#     name=input("请输入姓名")
#     age=int(input("请输入年龄"))
#     address=input("请输入地址")
#     stu=student(name,age,address)
#     print(f"姓名{stu.name},年龄{stu.age},地址{stu.address}")
# class Phone:
#     __is_5g_enable=True
#     def __chack_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print("5g关闭,使用4g网络")
#     def call_by_5g(self):
#         self.__chack_5g()
#         print("正在通话中")
# phone=Phone()
# phone.call_by_5g()
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#         print(f"大家好,我叫{self.name},今年{self.age}岁")
#
# class Student(Person):
#     def __init__(self,score):
#         super().__init__(self,name,age)
#         self.score=score
#     def get_score(self):
#         print(f"学生{self.name}的分数是{self.score}")
# import random
# a=random.randint(2,8)
# print(a)
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
# def have_people(animal):
#     animal.speak()
# dog=Dog()
# cat=Cat()
# have_people(dog)
# have_people(cat)
import warnings
warnings.filterwarnings("ignore")
import json
import re
import requests

class Student():
    def __init__(self,name,ch,ma,en,sentense):
        self.name=name
        self.ch=ch
        self.ma=ma
        self.en=en
        self.sentense=sentense

    def __str__(self):
        return f"学生{self.name}的语文成绩为{self.ch},数学成绩为{self.ma},英语成绩为{self.en}，名言：{self.sentense}"

    def update_score(self,ch=None,ma=None,en=None):
        if ch is not None:
            self.ch=ch
        if ma is not None:
            self.ma = ma
        if en is not None:
            self.en = en

    def to_dict(self):
        return{
            "name":self.name,
            "ch":self.ch,
            "ma":self.ma,
            "en":self.en,
            "sentense": self.sentense
        }

class Management():
    def __init__(self):
        self.student_list=[]
        self.load_file()
        # 重点修复：英文减号！解决姓名正则校验失败
        self.reg_name = r'^[\u4e00-\u9fa5]{2,10}$'

    def get_sentence(self):
        try:
            # verify=False 关闭ssl证书校验
            r = requests.get("https://api.quotable.io/random", timeout=3, verify=False)
            r.raise_for_status()
            data = r.json()
            # 同时返回名言+作者，你可以在__str__里展示
            return f"{data['content']} ——{data['author']}"
        except:
            return "好好学习，天天向上"

    def save_file(self):
        data=[stu.to_dict() for stu in self.student_list]
        try:
            with open("data.json","w",encoding="UTF-8")as f:
                json.dump(data,f,ensure_ascii=False,indent=2)
        except Exception as e:
            print(f"保存文件失败,错误{e}")

    def load_file(self):
        try:
            with open("data.json","r",encoding="UTF-8")as f:
                data=json.load(f)
                for d in data:
                    # 读取时增加sentense参数
                    stu=Student(d["name"],d["ch"],d["ma"],d["en"],d["sentense"])
                    self.student_list.append(stu)
        except FileNotFoundError:
            print("文件未找到,新建系统")
        except Exception as e:
            print(f"加载文件失败,错误{e}")

    def add_student(self):
        name=input("请输入学生姓名：").strip()
        if not re.fullmatch(self.reg_name,name):
            print("录入失败,名字必须是2-10个汉字")
            return
        for s in self.student_list:
            if s.name==name:
                print("学生已存在")
                return
        try:
            ch = int(input("请输入学生语文成绩："))
            ma = int(input("请输入学生数学成绩："))
            en = int(input("请输入学生英语成绩："))
        except ValueError:
            print("分数必须是数字")
            return
        if 0<=ch<=100 and 0<=ma<=100 and 0<=en<=100:
            sentense=self.get_sentence()
            stu=Student(name,ch,ma,en,sentense)
            self.student_list.append(stu)
            print("添加成功")
            self.save_file()
        else:
            print("分数应在0-100之间")

    def update_stu(self):
        name = input("请输入学生姓名：").strip()
        for s in self.student_list:
            if s.name==name:
                try:
                    ch = int(input("请输入学生语文成绩："))
                    ma = int(input("请输入学生数学成绩："))
                    en = int(input("请输入学生英语成绩："))
                except ValueError:
                    print("分数必须是数字")
                    return
                if 0 <= ch <= 100 and 0 <= ma <= 100 and 0 <= en <= 100:
                    s.update_score(ch,ma,en)
                    print(f"修改后的成绩为{s}")
                    self.save_file() # 修改后保存
                    return
                else:
                    print("分数应在0-100之间")
        else:
            print("未找到该学生")

    def delete_stu(self):
        name = input("请输入学生姓名：").strip()
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                self.save_file() # 删除后保存
                return
        else:
            print("未找到该学生")

    def show_stu(self):
        name = input("请输入学生姓名：").strip()
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        else:
            print("未找到该学生")

    def print_stu(self):
        if not self.student_list:
            print("没有学生")
        else:
            for s in self.student_list:
                print(f"学生信息：{s}")

    def calc_stu(self):
        if not self.student_list:
            print("没有学生")
            return
        ch_score=[]
        ma_score=[]
        en_score=[]
        for s in self.student_list:
            ch_score.append(s.ch)
            ma_score.append(s.ma)
            en_score.append(s.en)
        ch_max, ch_min = max(ch_score), min(ch_score)
        ma_max, ma_min = max(ma_score), min(ma_score)
        en_max, en_min = max(en_score), min(en_score)
        ch_avg = sum(ch_score) / len(ch_score)
        ma_avg = sum(ma_score) / len(ma_score)
        en_avg = sum(en_score) / len(en_score)

        ch_max_stu = (s.name for s in self.student_list if s.ch  == ch_max)
        ch_min_stu = (s.name for s in self.student_list if s.ch  == ch_min)
        ma_max_stu = (s.name for s in self.student_list if s.ma  == ma_max)
        ma_min_stu = (s.name for s in self.student_list if s.ma  == ma_min)
        en_max_stu = (s.name for s in self.student_list if s.en  == en_max)
        en_min_stu = (s.name for s in self.student_list if s.en  == en_min)

        print("=" * 40)
        print(f"语文最高分: {ch_max} 分，学生: {'、'.join(ch_max_stu)}")
        print(f"语文最低分: {ch_min} 分，学生: {'、'.join(ch_min_stu)}")
        print(f"语文平均分: {ch_avg:.2f} 分")
        print("-" * 40)
        print(f"数学最高分: {ma_max} 分，学生: {'、'.join(ma_max_stu)}")
        print(f"数学最低分: {ma_min} 分，学生: {'、'.join(ma_min_stu)}")
        print(f"数学平均分: {ma_avg:.2f} 分")
        print("-" * 40)
        print(f"英语最高分: {en_max} 分，学生: {'、'.join(en_max_stu)}")
        print(f"英语最低分: {en_min} 分，学生: {'、'.join(en_min_stu)}")
        print(f"英语平均分: {en_avg:.2f} 分")
        print("=" * 40)

    def run(self):
        print("欢迎使用学生管理系统")
        while True:
            print("""#############教务系统#############
#         1.添加学生信息
#         2.修改学生信息
#         3.删除学生信息
#         4.查询学生信息
#         5.列出所有学生信息
#         6.统计班级成绩
#         7.退出教务系统
###################################""")
            try:
                choice = int(input("请选择你要执行的操作(1-7)："))
                match choice:
                    case 1:
                        self.add_student()
                    case 2:
                        self.update_stu()
                    case 3:
                        self.delete_stu()
                    case 4:
                        self.show_stu()
                    case 5:
                        self.print_stu()
                    case 6:
                        self.calc_stu()
                    case 7:
                        print("感谢使用")
                        break
                    case _:
                        print("输入错误，请输入1~7")
            except ValueError:
                print("请输入1-7的数字")
            except Exception as e:
                print(f"程序出错了,错误{e}")

if __name__ == '__main__':
    m = Management()
    m.run()












