
import pickle

import sys

sys.path.insert(0, '/Users/devid/Documents/src7')

from faces1 import send2

a = send2()

continue1 = False

with open('/Users/devid/Documents/src7/cache/conf.conf', 'rb') as data:
    conf = pickle.load(data)
    conf = conf.decode('ascii')
    conf = int(conf)
print("B: ",str(conf))

b = a-3

while b < a+3:
    print(b)
    if b == conf:
        continue1 = True
        break
    else:
        b += 1
    
print(continue1)

while continue1:

    import sqlite3
    import pickle
    import sys
    import numpy as np
    import getpass

    sys.path.insert(1,'/Users/devid/Documents/src7/linked_list')
    sys.path.insert(2,'/Users/devid/Documents/src7/gamal')

    from c import linked
    from c import rotate_list_inv
    from g import main1

    conn = sqlite3.connect('user_encrypted_data.db')

    cursor = conn.execute("select ID, NODO from DATA")

    for fila in cursor:
        print("User: ", f'{fila[0]}', "    Data: ", fila[1])


    conn.close()

    usr1 = input("User to use: ")
    slec = input("Data to Unlock: ")
    pasw1 = input("Password to Unlock: ")

    with open(f'/Users/devid/Documents/src7/cache/{slec}.data', 'rb') as data:
        matrix = pickle.load(data)

    with open(f'/Users/devid/Documents/src7/cache/{slec}.node', 'rb') as node:
        linked = pickle.load(node)

    linked2 = rotate_list_inv(linked, conf)
    print('[Message to Decrypt]: ')

    print('--------')

    print(linked2)

    print('--------')


    matrix_b = np.array([], dtype = int)
    current = linked2
    while current != None:
        wa = main1(current.data[0], current.data[1], current.data[2], current.data[3])
        a1 = ''
        a2 = ''
        for i in range(len(wa)):
            if wa[i] == ' ':
                a1 = int(wa[:i])
                a2 = int(wa[i+1:])
        matrix_b = np.append(matrix_b,matrix[a1][a2])
        wa = ''
        current = current.next
    power1 = len(usr1) ** len(matrix_b)

    def final_msg(a,b):
        final_msg = ''
        for i in a:
            ay = round( i / power1)
            if ay <= 9:
                final_msg += ''.join(str(ay))
            else:
                final_msg += ''.join(chr(ay))
        if final_msg[:len(b)] == b:
            print("[Message]: ",final_msg[len(b)+1:])
        else:
            print("Wrong password! An error ocurred!")
            
    for i in pasw1:
        if i == '0':
            pasw1 = pasw1.replace('0', str(len(usr1)))
    final_msg(matrix_b, pasw1)
    continue1 = False
