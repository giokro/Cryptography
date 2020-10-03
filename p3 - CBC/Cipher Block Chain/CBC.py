"""
AES is a block cipher, which means it divides a message into different sized blocks (128 bit, 256 bit, so on) and encrypts it with a key.
The same key is used for every block.

CBC stands for "Cipher Block Chain", which basically means that each new block is XORed with the last ciphertext block before it's encrypted with the key.

IV stands for "Initialization Vector", which is just a random 16 byte (size of the block) long thing which is XORed with the first block (Because there's nothing before it to be used as part of an XOR). This can be called the 0th block. It is used to put randomness in the ciphers so the same text encrypted twice won't have the same output.

"""

from Crypto.Cipher import AES
from Crypto import Random

key = "1234569990123456"
message = "chiqashia chaqceuli mteli tqveni epoqa, peradebi ar unda, shav-tetrebic eyopa"

def splitIntoX(message, x):
	lenM = len(message)
	messages = []
	string = ""

	for i in range(lenM):
		index = i+1

		if index % x == 0:
			string += str(message[i])
			messages.append(string)
			string = ""
		elif index == lenM:
			string += str(message[i])
			messages.append(string)
		else:
			string += str(message[i])

	while len(messages[-1]) != x:
		messages[-1] += " "

	return messages


arr = splitIntoX(message, 16)

def encryptor(arr, key):
	IV = Random.new().read(16)
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	tempArr = []
	f = open("CBC_e.txt", "wb")

	for i in range(len(arr)):
		tempArr.append(encryptor.encrypt(arr[i]))
		f.write(tempArr[i])
		
	tempArr.insert(0,IV)

	return tempArr

def decryptor(arr, key):
	IV = arr[0]
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	plaintext = ""

	for i in range(len(arr)-1):
		plaintext += decryptor.decrypt(arr[i+1]).decode("utf-8")
	
	return(plaintext)

eArr = encryptor(arr,key)
plaintext = decryptor(eArr, key)

print(plaintext)





	
