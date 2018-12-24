import requests
from bs4 import BeautifulSoup
import xlrd
from xlutils.copy import copy


def get_one_page(url):
    response=requests.get(url)
    return response.text


def parse_on_page(html):
    soup=BeautifulSoup(html,'html.parser')
    for item in soup.select('tr')[3:-1]:
        yield {
            'value':item.select('td input')[0]['value']
        }


def parse_go_on_page(html):
    soup=BeautifulSoup(html,'html.parser')
    yield {
        "sug": soup.select('td')[4].text,
        "reply": soup.select('td')[5].text,
    }


def go_on_paser():
    f = xlrd.open_workbook("../file/回音壁信息.xls", formatting_info=True)
    wb = copy(f)
    ws = wb.get_sheet(0)
    row0 = ["问题内容", "回复"]
    for j in range(6, len(row0) + 6):
        ws.write(0, j, row0[j - 6])
    i = 0
    for k in range(1, 932):
        url = 'http://oa.dlmu.edu.cn/echoWall/listEchoWall.do?page='+str(k)
        html = get_one_page(url)
        for item in parse_on_page(html):
            url_x = 'http://oa.dlmu.edu.cn/echoWall/detailLetter.do?pkId=' + item['value']
            html_x = get_one_page(url_x)
            for item_x in parse_go_on_page(html_x):
                ws.write(i + 1, 6, item_x['sug'])
                ws.write(i + 1, 7, item_x['reply'])
                print("正在保存")
                i += 1
    wb.save("../file/回音壁信息.xls")


def main():
    go_on_paser()

if __name__ == '__main__':
    main()
