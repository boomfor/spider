# -*- coding:utf-8 -*-
import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
warnings.filterwarnings(action='ignore',category=FutureWarning,module='gensim')
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def train_w():
    sentences = LineSentence('../file/after_fenci.txt')
    model = Word2Vec(sentences, size=128)
    model.save('../file/tarining')


def similarity():
    model = Word2Vec.load('../file/tarining')
    # pro = input("请输入您想搜索的内容:")
    # items = model.most_similar(pro)
    # for item in items:
    #     print(item)


if __name__ == '__main__':
    train_w()
    similarity()