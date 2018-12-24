import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time
import numpy as np
from collections import defaultdict
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False


def readexcel():
    data = pd.read_excel("../file/回音壁信息.xls")
    return data


def postmail():
    data = readexcel()
    postm_d =data.提交信箱.value_counts()
    values = list(postm_d.values[0:10])
    values.append(sum(postm_d[10:]))
    labels = list(postm_d.index[0:10])
    labels.append("其它")
    explode = [0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    plt.title("各信箱分布统计表", fontsize=20)
    plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('../image/postmail.png')


def posttime_count():
    time_count = defaultdict(int)
    data = readexcel()
    posttime = data.提交时间
    for i in range(len(posttime.index)):
        a = time.strptime(posttime[i], "%Y-%m-%d %H:%M")
        m = a[1]
        time_count[m] += 1
    for key, value in time_count.items():
        print(key, value)
    plt.title("各个月份提出问题的数目")
    plt.pie(time_count.values(), labels=time_count.keys(),autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('../image/m_time.png')


def year_posttime_count():
    time_count = defaultdict(int)
    data = readexcel()
    posttime = data.提交时间
    for i in range(len(posttime.index)):
        a = time.strptime(posttime[i], "%Y-%m-%d %H:%M")
        y, m = a[0:2]
        if y == 2017:
            if m < 4:
                time_count[17_1] += 1
            elif m < 7:
                time_count[17_2] += 1
            elif m < 10:
                time_count[17_3] += 1
            else:
                time_count[17_4] += 1
        elif y == 2016:
            if m < 10:
                time_count[16_3] += 1
            else:
                time_count[16_4] += 1
        else:
            if m < 4:
                time_count[18_1] += 1
            elif m < 7:
                time_count[18_2] += 1
            elif m < 10:
                time_count[18_3] += 1
            else:
                time_count[18_4] += 1
    index = np.arange(3)
    bw = 0.2
    plt.title("每年横向比较")
    value = [0,time_count[17_1],time_count[18_1]]
    value2 = [0,time_count[17_2],time_count[18_2]]
    value3 = [time_count[16_3],time_count[17_3],time_count[18_3]]
    value4 = [time_count[16_4],time_count[17_4],time_count[18_4]]
    plt.axis([0, 3, 0, 1400])
    plt.bar(index, value, bw, color='b')
    plt.bar(index+bw, value2, bw, color='r')
    plt.bar(index+2*bw, value3, bw, color='g')
    plt.bar(index+3*bw, value4, bw, color='k')
    plt.xticks(index+1.5*bw,['2016','2017','2018'])
    plt.xlabel("年份")
    plt.ylabel("数量")
    plt.legend(['第一季度', '第二季度', '第三季度', '第四季度'], loc=1)
    plt.savefig('../image/y_season_time.png')
    plt.show()

def time_a():
    time_num = defaultdict(int)
    data = readexcel()
    time_d = data.回复时间差
    for i in range(len(time_d.index)):
        if int(time_d[i]) < 24:
            time_num['1_day'] += 1
        elif int(time_d[i]) < 48:
            time_num['2_days'] += 1
        elif int(time_d[i]) < 72:
            time_num['3_days'] += 1
        elif int(time_d[i]) < 96:
            time_num['4_days'] += 1
        else:
            time_num['others'] += 1
    plt.title("回复时间统计")
    plt.pie(time_num.values(), labels=time_num.keys(),autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('../image/time.png')
    plt.show()

if __name__ == '__main__':
    postmail()
    # time_a()
    # posttime_count()
    # year_posttime_count()
