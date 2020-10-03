from Crypto.Util import number
from random import randint
from fractions import gcd

def key_gen(key_len=8, p=0, q=0):
	
	# step 1 - get p & q
	while p == q:
		p = number.getPrime(key_len)
		q = number.getPrime(key_len)
	
	# step 2
	n = p*q
	
	# step 3
	phi = (p-1)*(q-1)

	# step 4 - e must be in range(1, phi-1) & e and phi must be co-primes
	e = randint(1, phi-1)
	while gcd(e, phi) != 1:
		e = randint(1, phi-1)

	# step 5 - (d*e) % phi must be 1
	d = randint(1, 200000)
	while (d*e) % phi != 1:
		d = randint(1, 200000)

	print("Private key:", d, "Public key:", e)

	return d, e, n

def encrypt(plaintext, e, n):
	ciphertext = []

	for i in plaintext:
		temp = (ord(i)**e) % n
		ciphertext.append(temp)

	return ciphertext

def decrypt(ciphertext, d, n):
	plaintext = ""

	for i in ciphertext:
		temp = (i**d) % n
		plaintext += chr(temp)

	return plaintext

if __name__ == "__main__":
	
	plaintext = "Power in the money\nMoney in the power"

	keys = key_gen()

	ciphertext = encrypt(plaintext, keys[1], keys[2])
	print(ciphertext)

	print(decrypt(ciphertext, keys[0], keys[2]))




