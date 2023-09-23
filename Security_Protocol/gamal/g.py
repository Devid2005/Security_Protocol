import random
from math import pow


def power(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b % 2 != 0:
			x = (x * y) % c;
		y = (y * y) % c
		b = int(b / 2)

	return x % c

def decrypt(en_msg, p, key, q):

	dr_msg = []
	h = power(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))
		
	return dr_msg

def main1(en_msg, p, key, q):
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    return dmsg

