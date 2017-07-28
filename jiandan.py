import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    html=html.decode('utf-8')
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
      urllib.request.urlretrieve('https:'+imgurl,'./img/%s.jpg' % x)
      x += 1
    return imglist

html = getHtml("http://jandan.net/ooxx")

print(getImg(html))
