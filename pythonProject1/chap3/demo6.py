# 公众号：MarkerJava
# 开发时间：2020/10/7 22:00

import requests  # 导入库
from bs4 import BeautifulSoup  # 导入bs4
import re
import os
from kkb_tools import open_file


def get_novel_chapters():  # 获取小说每一章的链接
    root_url = "http://www.booksky.cc/26763.html"
    r = requests.get(root_url)  # 发送request请求
    r.encoding = "utf-8"  # 网页编码为utf-8
    soup = BeautifulSoup(r.text, "html.parser")  # 创建bs4对象，解析器用官方的html.parser
    data = []  # 创建一个列表保存每一章的链接
    for li in soup.find_all("li", ):  # 匹配所有li标签
        link = li.find("a", target="_blank", href=re.compile("read"))
        # 匹配所有的href带read字样的链接
        if not link:  # 如果没获取到链接，就忽略
            continue

        data.append(("http://www.booksky.cc%s" % link['href'], link.get_text()))
    return data  # 返回小说所有章节的链接和标题，link.get_text()


def get_chapter_content(url):  # 从所有小说的链接中解析每一章链接中的小说正文部分和标题
    r = requests.get(url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        return soup.find("div", class_='content').get_text()  # 获取div标签里的文本get.text()
    except:  # 忽略没有获取到的小说文本的链接
        pass


if not os.path.exists('data'):
    os.makedirs('data')
for chapter in get_novel_chapters()[:10]:
    url, title = chapter  # 从data文件中读取每一章小说的链接和标题并赋值
    print(chapter)
    with open("data/%s.txt" % title, "w") as fout:  # 写入小说文本文件名就是标题名
        try:  # 忽略空白文本
            fout.write(get_chapter_content(url))
        except:
            pass
    print("data/%s.txt" % title)  # 打印已经写入小说的文本
    import zipfile

    z = zipfile.ZipFile('data.zip', 'w', zipfile.ZIP_DEFLATED)
    startdir = "data"
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            z.write(os.path.join(dirpath, filename))
    z.close()
    open_file('data.zip')