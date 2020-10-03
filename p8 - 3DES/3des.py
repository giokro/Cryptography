from des import DesKey

def seperateKey(key0):
	if(len(key0)!=24):
		print("Key length must be 24")
		return
	else:
		keys = []

		temp = ""
		for i in range(24):
			if(i==7 or i==15 or i==23):
				temp += key0[i]
				keys.append(temp)
				temp = ""
			else:
				temp += key0[i]

	return keys


def des3():
	
	mode = input("Input mode - e or d: ")
	key0 = input("Input a key with length 24: \n")

	keys = seperateKey(key0)

	key1 = DesKey(keys[0].encode())
	key2 = DesKey(keys[1].encode())
	key3 = DesKey(keys[2].encode())

	if(mode=="e"):
		data = input("Input data: \n")

		s1 = key1.encrypt(data.encode(), padding=True)
		s2 = key2.decrypt(s1, padding=True)
		s3 = key3.encrypt(s2, padding=True)

		f = open("ciphertext", "wb")
		f.write(s3)

		print("Encryption done")

	elif(mode=="d"):
		filename = input("ciphertext filename: ")
		f = open(filename, "rb")
		lines = f.readlines()
		
		s3 = key3.decrypt(lines[0], padding=True)
		s2 = key2.encrypt(s3, padding=True)
		s1 = key1.decrypt(s2, padding=True)

		print(s1)
	else:
		print("Mode not supported")


if __name__=="__main__":
	des3()


