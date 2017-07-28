import re
import urllib.request

GANK = "http://gank.io/api/data/%E7%A6%8F%E5%88%A9/500/1"
DB_BREAST = "http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset="
DB_BUTT = "http://www.dbmeinv.com/dbgroup/show.htm?cid=6&pager_offset="
DB_SILK = "http://www.dbmeinv.com/dbgroup/show.htm?cid=7&pager_offset="
DB_LEG = "http://www.dbmeinv.com/dbgroup/show.htm?cid=3&pager_offset="
DB_RANK = "http://www.dbmeinv.com/dbgroup/rank.htm?pager_offset="

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
      urllib.request.urlretrieve(imgurl,'./img/%s.jpg' % x)
      x += 1
    return imglist

html = getHtml('http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset=1')

print(getImg(html))
