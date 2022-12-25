import http.client

conn = http.client.HTTPSConnection('beda.pnzgu.ru')
conn.request("GET", "/anatoly/")
r=conn.getresponse()
print('Proto : ', r.version)
print('Code :', r.status)
print('Status :', r.reason)
print('---------- HEADERS ----------')
print(r.headers)
print('----------- BODY ------------')
print(r.read().decode())
conn.close()
