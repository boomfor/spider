import requests
from bs4 import BeautifulSoup
import xlwt
import time
import datetime


def get_one_page(url):
    response = requests.get(url)
    return response.text


def parse_on_page(html):
    soup = BeautifulSoup(html,'html.parser')
    i=1
    for item in soup.select('tr')[3:-1]:
        yield {
            'posttime': item.select('td')[i].text.strip(),
            'title': item.select('td a')[0].text.strip(),
            'xinxiang': item.select('td')[i+2].text.strip(),
            'responser': item.select('td')[i+3].text.strip(),
            'response_time': item.select('td')[i+4].text.strip(),
        }


def write_to_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('回音壁', cell_overwrite_ok=True)
    sheet1.col(0).width = 256*20
    sheet1.col(1).width = 256 * 30
    sheet1.col(2).width = 256 * 14
    sheet1.col(4).width = 256 * 20
    sheet1.col(5).width = 256 * 10
    row0 = ["提交时间", "提交名称", "提交信箱", "回复人", "回复时间", "回复时间差/h"]
    for j in range(0, len(row0)):
        sheet1.write(0, j, row0[j])
    i = 0
    for k in range(1, 932):
        url = 'http://oa.dlmu.edu.cn/echoWall/listEchoWall.do?page='+str(k)
        html = get_one_page(url)
        print("正在保存%d页" % k)
        for item in parse_on_page(html):
            sheet1.write(i+1, 0, item['posttime'])
            sheet1.write(i+1, 1, item['title'])
            sheet1.write(i + 1, 2, item['xinxiang'])
            sheet1.write(i + 1, 3, item['responser'])
            sheet1.write(i + 1, 4, item['response_time'])
            a = time.strptime(item['posttime'], "%Y-%m-%d %H:%M")
            b = time.strptime(item['response_time'], "%Y-%m-%d %H:%M")
            y, m, d, H, M = a[0:5]
            da = datetime.datetime(y, m, d, H, M)
            y, m, d, H, M = b[0:5]
            db = datetime.datetime(y, m, d, H, M)
            sheet1.write(i + 1, 5, (db - da).total_seconds() / 60 / 60)
            i += 1
    f.save("../file/回音壁信息.xls")


def main():
    write_to_excel()

if __name__ == '__main__':
    main()
