#encoding=utf-8
import copy
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import pandas as pd
# print("please input name list")
# input_list = input()
# name_list = input_list.split(',')
# print("please input days number:")
# all_days = int(input())
fr = open("name_list.txt", 'r', encoding="utf-8").readlines()
print("read input name_list.txt")
name_list = fr[0].strip().split(',')
all_days = int(fr[1].strip())
# name_list = ["张三-男","李四-男","王美-女","赵云-男","丽丽-女","李航-男","王云-女","孙杨-男","孙楠-男","李明-男","任雯-女"]

name_list_tmp = copy.deepcopy(name_list)
results = {}
morning= []
afternoon = []
evening = []
day_count = 0
index = 0
pre_queue = []
find = False
while day_count < all_days:
    find = False
    if not name_list_tmp:
        name_list_tmp = name_list_tmp + copy.deepcopy(name_list)
    morning.append(name_list_tmp.pop(0).split('-')[0])
    if not name_list_tmp:
        name_list_tmp = name_list_tmp + copy.deepcopy(name_list)
    afternoon.append(name_list_tmp.pop(0).split('-')[0])
    if not name_list_tmp:
        name_list_tmp = name_list_tmp + copy.deepcopy(name_list)
    for i in range(len(name_list_tmp)):
        if name_list_tmp[i].split('-')[1] == "男":
            find = True
            evening.append(name_list_tmp[i].split('-')[0])
            name_list_tmp.pop(i)
            break
    if not find:
        name_list_tmp = name_list_tmp + copy.deepcopy(name_list)
        for i in range(len(name_list_tmp)):
            if name_list_tmp[i].split('-')[1] == "男":
                find = True
                evening.append(name_list_tmp[i].split('-')[0])
                name_list_tmp.pop(i)
                break
    day_count += 1

idx = list(range(all_days))
results["日期"] = idx
results["上午"]= morning
results["下午"]= afternoon
results["晚上"]= evening

df_out = pd.DataFrame(results, index=idx)
print("output schedule.xls")
df_out.to_excel("./schedule.xls", index=None, columns=["日期", "上午", "下午", "晚上"])
# df_out.to_csv("./schedule.tsv", index=None, sep='\t', columns=["日期", "上午", "下午", "晚上"])