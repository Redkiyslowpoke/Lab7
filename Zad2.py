from socket import *

def poisk(fam):
    f=open('narod.txt', 'r+', encoding='utf-8')
    spis=list(f)
    f.close()
    name = None
    if fam.encode('utf-8')==b'\n':
        name = 'Вы не ввели фамилию\n'
    else:
        for i in range(len(spis)):
            if spis[i].split()[1] == fam.rstrip().capitalize(): 
                name = 'Привет, ' + spis[i].split()[2] + '\n'
        if name == None:
            name ='ERROR\n'
    return name

with socket(type = SOCK_DGRAM) as svr:
    svr.bind(('',7777))
    while True:
        fam, address = svr.recvfrom(4096)
        svr.sendto(poisk(fam.decode('utf-8')).encode('utf-8'), address)
