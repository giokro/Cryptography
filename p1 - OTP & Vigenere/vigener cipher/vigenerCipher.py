def vigenerCipher():
	
	wch = input("Type \"e\" to encipher and \"d\" to decipher: ")

	if wch == "e":
		ciphertext = ""

		s1 = input("Enter plaintext:\n")
		len1 = len(s1)
		s2 = input("Enter key: \n")
		len2 = len(s2)

		arr = []
		index = 0
		for i in range(len1):
			if index+1 == len2:
				arr.extend([[s1[i],s2[index]]])
				index = 0
			else:
				arr.extend([[s1[i],s2[index]]])
				index += 1

		f = open("ciphertext.txt", "w+")
		for i in range(len1):
			a = ord(arr[i][0])-96
			b = ord(arr[i][1])-96
			temp = (a+b)%26			
			if temp == 0:
				temp = 26

			ciphertext += chr(temp+96)

		print(ciphertext)
		f.write(ciphertext)
		f.close()


	elif wch == "d":
		plaintext = ""

		s1 = input("Enter ciphertext:\n")
		len1 = len(s1)
		s2 = input("Enter key: \n")
		len2 = len(s2)

		arr = []
		index = 0
		for i in range(len1):
			if index+1 == len2:
				arr.extend([[s1[i],s2[index]]])
				index = 0
			else:
				arr.extend([[s1[i],s2[index]]])
				index += 1

		f = open("plaintext.txt", "w+")
		for i in range(len1):
			a = ord(arr[i][0])-96
			b = ord(arr[i][1])-96
			temp = (a-b)%26
			if temp == 0:
				temp = 26

			plaintext += chr(temp+96)

		print(plaintext)
		f.write(plaintext)
		f.close()

	else:
		print("input must be \"e\" or \"d\"")

vigenerCipher()

