print("欢迎使用学生管理系统")
print("""############教务系统#########
#         1.添加学生信息
#         2.修改学生信息
#         3.删除学生信息
#         4.查询学生信息
#         5.列出所有学生信息
#         6.统计班级成绩
#         7.退出教务系统
###################################""")
stu_message={}
while True:
    choice=int(input("请选择要执行的操作(1-7)"))
    match choice:
        case 1:
            stu_name=input("请输入学生姓名")
            stu_ch=int(input("请输入学生语文成绩"))
            stu_ma=int(input("请输入学生数学成绩"))
            stu_en=int(input("请输入学生英语成绩"))
            if stu_name in stu_message:
                print("该学生已存在")
            else:
                stu_message[stu_name]=[stu_ch,stu_ma,stu_en]
                print("添加成功")
        case 2:
            stu_name = input("请输入学生姓名")
            if stu_name not in stu_message:
                print("该学生不存在")
                continue
            stu_ch=input("请输入学生语文成绩")
            stu_ma=input("请输入学生数学成绩")
            stu_en=input("请输入学生英语成绩")
            stu_message[stu_name] = [stu_ch, stu_ma, stu_en]
            print("修改成功")

        case 3:
            stu_name = input("请输入学生姓名")
            if stu_name not in stu_message:
                print("该学生不存在")
            else:
                del stu_message[stu_name]
                print("删除成功")
        case 4:
            name = input("请输入学生姓名")
            if name not in stu_message:
                print("该学生不存在")
            else:
                stu_info=stu_message[name]
                print(f"学生姓名:{name}, 语文:{stu_info[0]}, 数学:{stu_info[1]}, 英语:{stu_info[2]}")
        case 5:
            if not stu_message:
                print("无学生信息")
                continue
            for name in stu_message:
                stu_info=stu_message[name]
                print(f"学生姓名:{name}, 语文:{stu_info[0]}, 数学:{stu_info[1]}, 英语:{stu_info[2]}")
        case 6:
            if not stu_message:
                print("无学生信息")
                continue
            score_ch=[]
            score_ma=[]
            score_en=[]
            for name,score in stu_message.items():
                score_ch.append(score[0])
                score_ma.append(score[1])
                score_en.append(score[2])
            ch_max,ch_min=max(score_ch),min(score_ch)
            ma_max,ma_min=max(score_ma),min(score_ma)
            en_max,en_min=max(score_en),min(score_en)
            ch_avg=sum(score_ch)/len(score_ch)
            ma_avg=sum(score_ma)/len(score_ma)
            en_avg=sum(score_en)/len(score_en)
            ch_max_stu=(name for name,score in stu_message.items() if score[0]==ch_max)
            ch_min_stu=(name for name,score in stu_message.items() if score[0]==ch_min)
            ma_max_stu=(name for name,score in stu_message.items() if score[1]==ma_max)
            ma_min_stu=(name for name,score in stu_message.items() if score[1]==ma_min)
            en_max_stu=(name for name,score in stu_message.items() if score[2]==en_max)
            en_min_stu=(name for name,score in stu_message.items() if score[2]==en_min)
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
        case 7:
            print("感谢使用")
            break
        case _:
            print("输入错误")








