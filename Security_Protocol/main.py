import sys
import pickle
sys.path.insert(0, '{path_file}')

from faces import send

conf = str(send())
conf = conf.encode('ascii')
print(conf)

with open('{path_file}/cache/conf.conf', 'wb') as data:
    pickle.dump(conf, data)

with open('{path_file}/cache/conf.conf', 'rb') as data:
    conf = pickle.load(data)
    conf = conf.decode('ascii')
    conf = int(conf)

print(conf)
print(type(conf))

import random
import numpy as np
import getpass
import time
import datetime as dev
import sqlite3


sys.path.insert(1,'{path_file}/gamal')
sys.path.insert(2,'{path_file}/linked_list')

from b import main
from c import linked


usr = input("Enter Username: ")

pass1 = input("Enter Password: ")
msg1 = input("Enter Message: ")

pasw  = pass1 + ": " + msg1
power = len(usr) ** len(pasw)

b = np.array([], dtype = int)
c = np.array([], dtype = int)

for i in pasw:
    if i.isdigit():
        a = int(i)
        if a == 0:
            a += len(usr)
        b = np.append(b,(a*power))
    else:
        b = np.append(b,(ord(i) * power))

times1 = dev.datetime.now()
times1 = times1.strftime("%Y-%m-%d-%H:%M:%S")

curr_time = round(time.time()*1000)

for i in range((conf*conf)- len(pasw)):
    a = random.randint(1, curr_time)
    c = np.append(c,a)

array = np.concatenate((b,c))

random.shuffle(array)
array = np.reshape(array, (round(conf), round(conf)))
print(array)

with open(f'{path_file}/cache/{times1}.data', 'wb') as data:
    pickle.dump(array, data)

c = ''
d = []
for i in b:
    index_x, index_y = np.where(array == i)
    c = str(index_x[0]),str(index_y[0])
    str1 = ' '.join(c)
    m = main(str1)
    d.append(m)

linked1 = linked(d, conf)
print('[Encrypted Message]: ')

print('--------')

print(linked1)

print('--------')

with open(f'{path_file}/cache/{times1}.node', 'wb') as node:
    pickle.dump(linked1, node)

conn = sqlite3.connect('user_encrypted_data.db')
try:
    conn.execute('''
            CREATE TABLE DATA
                (ID TEXT         NOT NULL,
                NODO            BLOB     NOT NULL);''')
    print ("Table created successfully")
except sqlite3.OperationalError:
    print("La tabla DATA ya existe")
conn.execute("INSERT INTO DATA (ID,NODO) VALUES (?,?)", (usr, times1))
conn.commit()

cursor = conn.execute("select ID, NODO from DATA")

for fila in cursor:
    print(fila[1])

conn.close()





