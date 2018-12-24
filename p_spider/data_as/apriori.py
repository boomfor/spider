import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from collections import defaultdict,Counter

class Window:
    def __init__(self):
        with open('../file/after_fenci.txt',encoding='utf-8') as f:
            self.title_l = [[line.strip()] for line in f.readlines()]
        # self.dataSet=[]
        self.dataSet=self.title_l
        self.dataSet_t=[]
        self.N = None  # 购物篮数据的总数
        self.D = None  # 频繁项集的最大项个数
        self.fre_list = []  # 频繁项集，[[[],[]],[[],[]]]
        self.sup_list = []  # 存储每个频繁项的支持度
        self.fre_dict = defaultdict(lambda: 0)
        self.rules_dict = defaultdict(lambda: 0)
        self.window=tk.Tk()
        self.window.title("算法")
        self.window.geometry("900x600+250+10")
        self.checkbox_lable = tk.Label(self.window, text="请勾选订单上的商品", font=("宋体", 20))
        self.checkbox_lable.place(x=300,y=50)
        self.s_biscute=tk.IntVar()
        self.s_mike=tk.IntVar()
        self.s_bread=tk.IntVar()
        self.s_yoil=tk.IntVar()
        self.s_wine=tk.IntVar()
        self.s_cloth=tk.IntVar()
        self.biscute=tk.Checkbutton(self.window,text="饼干",onvalue=1,offvalue=0,variable=self.s_biscute)
        self.mike=tk.Checkbutton(self.window,text="牛奶",onvalue=1,offvalue=0,variable=self.s_mike)
        self.bread=tk.Checkbutton(self.window,text="面包",onvalue=1,offvalue=0,variable=self.s_bread)
        self.yoil=tk.Checkbutton(self.window,text="黄油",onvalue=1,offvalue=0,variable=self.s_yoil)
        self.wine=tk.Checkbutton(self.window,text="啤酒",onvalue=1,offvalue=0,variable=self.s_wine)
        self.cloth=tk.Checkbutton(self.window,text="尿布",onvalue=1,offvalue=0,variable=self.s_cloth)
        self.biscute.place(x=100,y=100)
        self.mike.place(x=200,y=100)
        self.bread.place(x=300,y=100)
        self.yoil.place(x=400,y=100)
        self.wine.place(x=500,y=100)
        self.cloth.place(x=600,y=100)
        self.submit_button=tk.Button(self.window,text="提交数据",width=15,height=1,command=self.submit)
        self.submit_button.place(x=250,y=150)
        self.watch_button = tk.Button(self.window, text="查看购物清单记录", width=15, height=1, command=self.watch)
        self.watch_button.place(x=500, y=150)
        self.sup=tk.StringVar()
        self.con = tk.StringVar()
        x_name = tk.Label(self.window, text="请输入最小支持度", font=("宋体", 10))
        x_name.place(x=450, y=220)
        x_txt = tk.Entry(self.window, textvariable=self.sup, width=8, font=("Arial", 15))
        x_txt.place(x=580, y=220)
        y_lable = tk.Label(self.window, text="请输入最小置信度", font=("宋体", 10))
        y_lable.place(x=450, y=270)
        y_txt = tk.Entry(self.window, textvariable=self.con, width=8, font=("Arial", 15))
        y_txt.place(x=580, y=270)
        self.textarea = scrolledtext.ScrolledText(self.window, width=40, height=10, font=("宋体", 10))
        self.textarea.place(x=100, y=200)
        self.ap=tk.Button(self.window,text="开始关联",width=15,height=1,command=self.start_ap)
        self.ap.place(x=520,y=320)
        self.result=scrolledtext.ScrolledText(self.window, width=40, height=10, font=("宋体", 10))
        self.result.place(x=100,y=370)
        self.window.mainloop()

    def submit(self):
        self.dataSet_t.clear()
        if self.s_biscute.get()==1:
            self.dataSet_t.append("饼干")
        if self.s_wine.get()==1:
            self.dataSet_t.append("啤酒")
        if self.s_yoil.get()==1:
            self.dataSet_t.append("黄油")
        if self.s_bread.get()==1:
            self.dataSet_t.append("面包")
        if self.s_mike.get()==1:
            self.dataSet_t.append("牛奶")
        if self.s_cloth.get()==1:
            self.dataSet_t.append("尿布")
        self.dataSet.append(self.dataSet_t.copy())
        tk.messagebox.showinfo(title="数据提交成功",message="数据提交成功")

    def watch(self):
        self.textarea.delete(1.0,'end')
        for i in enumerate(self.dataSet):
            self.textarea.insert('end',str(i[0])+'  '+str(i[1])+'\n')


    def init_param(self):
        # 根据传入的数据初始化参数
        self.data = sorted(self.dataSet)
        self.N = len(self.data)
        self.D = 0
        item_counter = Counter()
        for itemset in self.data:
            if len(itemset) > self.D:
                self.D = len(itemset)
            item_counter += Counter(itemset)
        itemset = sorted(item_counter)  # 保证有序
        c1 = []
        sup_c1 = []
        for item in itemset:
            sup = item_counter[item] / self.N
            if sup >= float(self.sup.get()):
                c1.append([item])
                sup_c1.append(sup)
        self.fre_list.append(c1)
        self.sup_list.append(sup_c1)

    def apriori_fre_itemset(self):
        # 使用Apriori算法获取频繁项集
        for i in range(1, self.D):  # 逐渐增加频繁项大小
            ck_1 = self.fre_list[i-2]
            if len(ck_1) < 2:  # 若k-1频繁项集不足两个，则跳出循环
                break
            cand_ck_set = self.ck_itemset(i, ck_1)
            sup_ck = []
            ck = []
            for item in cand_ck_set:  # 计算ck的支持度
                sup = self.cal_sup(item)
                if sup >= float(self.sup.get()):
                    ck.append(item)
                    sup_ck.append(sup)

            if len(ck) > 0:
                self.fre_list.append(ck)
                self.sup_list.append(sup_ck)
        for ck, sup_ck in zip(self.fre_list, self.sup_list):
            for itemset, sup in zip(ck, sup_ck):
                self.fre_dict[tuple(itemset)] = sup

    def ck_itemset(self, ind, ck_1):
        cand_ck_set = []
        for i in range(len(ck_1)):  # 合并两个k-1频繁项集
            cand_ck = ck_1[i]
            for j in range(i + 1, len(ck_1)):
                if ck_1[i][:ind - 2] == ck_1[j][:ind - 2]:  # 若前k-2项相同则合并
                    cand_ck.append(ck_1[j][-1])  # 合并形成频繁k项
                    if self.prune(cand_ck, ck_1):  # 检查其他k-1项集是否为频繁项集,进而减枝
                        cand_ck_set.append(cand_ck.copy())
                    cand_ck.pop()
        return cand_ck_set

    def prune(self, cand_ck_item, ck_1):
        for item in cand_ck_item[:-2]:
            sub_item = cand_ck_item.copy()
            sub_item.remove(item)
            if sub_item not in ck_1:
                return False
        return True

    def cal_sup(self, item):
        # 支持度计数
        s = set(item)
        sup = 0
        for t in self.data:
            if s.issubset(t):
                sup += 1
        return sup / self.N

    def cal_conf(self, sxy, X):
        # 计算置信度, sxy为产生规则的频繁项集的支持度， X为规则前件
        return sxy / self.fre_dict[tuple(X)]

    def gen_rules(self):
        # 从频繁项集中提取规则
        for i in range(1, len(self.fre_list)):
            for ind, itemset in enumerate(self.fre_list[i]):
                cand_rules = []  # 由该频繁项集产生的规则的list, 记录规则前件
                sxy = self.sup_list[i][ind]
                for item in itemset:  # 初始化后件为1个项的规则
                    X = itemset.copy()
                    X.remove(item)
                    cand_rules.append(X)

                while len(cand_rules) > 0:
                    itemset_rules = []
                    for X in cand_rules:
                        conf = self.cal_conf(sxy, X)
                        if conf >=float(self.con.get()):
                            itemset_rules.append(X)
                            Y = list(set(itemset) - set(X))
                            Y = sorted(Y)
                            self.rules_dict[(tuple(X), tuple(Y))] = conf
                    cand_rules = self.apriori_rules(itemset_rules)

    def apriori_rules(self, itemset_rules):
        cand_rules = []
        for i in range(len(itemset_rules)):
            for j in range(i + 1, len(itemset_rules)):
                X = list(set(itemset_rules[i]) & set(itemset_rules[j]))  # 合并生成新的规则前件
                X = sorted(X)
                if X in cand_rules or len(X) < 1:
                    continue
                cand_rules.append(X)
        return cand_rules

    def start_ap(self):
        self.rules_dict.clear()
        self.fre_list.clear()
        self.fre_dict.clear()
        self.sup_list.clear()
        self.result.delete(1.0,'end')
        self.init_param()
        self.apriori_fre_itemset()
        self.gen_rules()
        print('产生的频繁项集和支持度如下:')
        self.result.insert('end','产生的频繁项集和支持度如下:'+'\n')
        for item in self.fre_dict:
            print(item, self.fre_dict[item])
            self.result.insert('end',str(item)+'   '+str(self.fre_dict[item])+'\n')
        self.result.insert('end', '\n'+'产生的关联规则如下:'+'\n')
        for i in self.rules_dict:
            self.result.insert('end',str(list(i[0]))+"==>"+str(list(i[1]))+'    '+str(self.rules_dict[i])+'\n')


def main():
    win=Window()

if __name__ == '__main__':
    main()