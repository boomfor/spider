from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
import gc


word_list = []
with open('../file/after_fenci.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        word_list.append(line.strip())


verctorizer = CountVectorizer()
transformer = TfidfTransformer()
tf_idf = transformer.fit_transform(verctorizer.fit_transform(word_list))
word = verctorizer.get_feature_names()
weight = tf_idf.toarray()

# with open('../file/vec.txt', 'w', encoding='utf-8') as f:
#     for j in range(len(word)):
#         f.write(word[j]+' ')
#     f.write('\r\n\r\n')
#     for i in range(len(weight)):
#         for j in range(len(word)):
#             f.write(str(weight[i][j])+' ')
#         f.write(word[j] + ' ')


clf = KMeans(n_clusters=6)
s = clf.fit(weight)


lables = []
i = 1
while i <= len(clf.labels_):
    lables.append(clf.labels_[i-1])
    i += 1

