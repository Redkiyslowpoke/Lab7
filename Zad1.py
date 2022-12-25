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
    
with create_server(('',7777)) as svr:
     while True:
        conn, address = svr.accept()
        conn.send('Напиши свою фамилию:\n'.encode('utf-8'))
        fam = conn.recv(4096).decode('utf-8')
        conn.send(poisk(fam).encode('utf-8'))
        conn.close()
