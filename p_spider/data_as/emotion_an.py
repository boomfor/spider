from nltk.sentiment.vader import SentimentIntensityAnalyzer


with open('../file/after_fenci.txt', encoding='utf-8') as f:
    title_l = [[line.strip()] for line in f.readlines()]

sid = SentimentIntensityAnalyzer()
finalScore = 0
for line in title_l[0:20]:
    print(line)
#     ss = sid.polarity_scores(line)
#     for k in sorted(ss):
#         print('{0}:{1}\n'.format(k,ss[k]),end=""
# )