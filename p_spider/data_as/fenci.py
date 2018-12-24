import pandas as pd
import jieba
jieba.load_userdict("../file/userdict.txt")


def readexcel():
    data = pd.read_excel("../file/回音壁信息.xls")
    return data


def fenci():
    data = readexcel()
    all_list=[]
    after_word = []
    title_l = data.提交名称.tolist()
    # procontent = data.问题内容
    # for i in range(len(procontent)):
    #     myword =procontent[i].strip()
    #     myword_w = myword.replace(" ","")
    #     title_l.append(myword_w.replace("\n", "").replace("  ",""))
    # for j in title_l:
    #     print(j)
    title_s = "\n".join(title_l)
    cut_lists = jieba.cut(title_s, cut_all=False)
    with open('../file/stopword.txt') as f:
        stopword_list = f.read().split('\n')
    for cut_word in cut_lists:
        if not(cut_word in stopword_list) and cut_word != '\n':
            after_word.append(cut_word)
        if cut_word == "\n":
            all_list.append(after_word)
            after_word = after_word[0:0]

    with open('../file/after_fenci.txt', 'w+', encoding='utf-8') as f:
        for wordlist in all_list:
            for word in wordlist:
                f.write(word+",")
            f.write("\n")


if __name__ == '__main__':
    fenci()