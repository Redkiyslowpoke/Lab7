import http.client
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    global pic
                    pic = attr[1]
                    return pic
def skach(pic):
    conn.request("GET", '/anatoly/' + pic)
    r = conn.getresponse()
    f = open('1.jpg', 'wb')
    f.write(r.read())                   
        
parser = MyParser()
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
conn.request('GET', '/anatoly/')
r = conn.getresponse()
parser.feed(r.read().decode())
parser.close()
skach(pic)
