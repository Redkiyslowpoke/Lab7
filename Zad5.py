import http.client
from html.parser import HTMLParser
def skach(pic,name):
    conn.request("GET", '/anatoly/' + pic)
    r = conn.getresponse()
    f = open(name + '.jpg', 'wb')
    f.write(r.read())                   

class MyParser_link(HTMLParser):
    global links
    links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    links.append(attr[1])
            return links                  
class MyParser_pic(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            global pic
            for attr in attrs:
                if attr[0] == 'src':
                    pic=(attr[1])
            return pic                        
        else:
            pic = None
            return pic
parser1 = MyParser_link()
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
conn.request('GET', '/anatoly/')
r = conn.getresponse()
parser1.feed(r.read().decode())
parser1.close()
for i in range(len(links)):               
    parser2 = MyParser_pic()
    conn.request('GET', '/anatoly/' + links[i])
    t = conn.getresponse()
    parser2.feed(t.read().decode())
    parser2.close()
    if pic != None:
        skach(pic,str(i+2))        
