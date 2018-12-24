import jieba.analyse
from wordcloud import WordCloud
from matplotlib import pyplot as plt


def generate_p():
    with open('../file/after_fenci.txt', encoding='utf-8') as f:
        s = f.read()
    heighweight_ws = jieba.analyse.textrank(s, 100, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
    keyword = ''
    for word, weight in heighweight_ws:
        keyword += word+' '
    stopword = ['公寓', '咨询', '建议', '问题']
    wc = WordCloud(font_path='D:\test\simheittf.ttf',
                   background_color='white',
                   width=800,
                   min_font_size=5,
                   max_font_size=95,
                   height=600,
                   stopwords=stopword
                   ).generate_from_text(keyword)
    plt.imshow(wc)
    plt.axis('off')
    wc.to_file('../image/wordcloud.png')
    plt.show()

if __name__ == '__main__':
    generate_p()