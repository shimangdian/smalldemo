import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = r'"url":"(.+?\.jpg)"'
    imgre = re.compile(reg)
    html=html.decode('utf-8')
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
      urllib.request.urlretrieve('https://www.bing.com'+imgurl,'./img/%s.jpg' % x)
      x += 1
    return imglist

html = getHtml("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=100&mkt=zh-CN")

print(getImg(html))
