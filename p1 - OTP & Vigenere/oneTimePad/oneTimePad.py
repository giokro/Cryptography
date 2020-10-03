def oneTimePad():
	output = []
	
	wch = input("Type \"e\" to encipher and \"d\" to decipher: ")

	if wch == "e":
		s1 = input("Enter plaintext:\n").encode()
		print("plaintext is", len(s1),"long")
		s2 = input("Enter key: \n").encode()
	
		while len(s1) != len(s2):
			print("They are not the same length!")
			s2 = input("Enter new key: \n").encode()

		zipped = list(zip(s1, s2))
		zipLen = len(zipped)

		f = open("ciphertext.txt", "w+")

		for i in range(zipLen):
			temp = zipped[i][0]^zipped[i][1]
			f.write(str(temp))
			f.write(",")
			output.extend([temp])

		f.close()
		print(output)


	elif wch == "d":
		string = ""

		f = open("ciphertext.txt", "r")
		lines = f.readlines()
		f.close()
		arr = lines[0].split(",")
		del arr[-1]
		arrLen = len(arr)
	
		print("Size should be", arrLen)
		key = input("Enter key: ").encode()

		while len(key) != arrLen:
			print("They are not the same length!")
			key = input("Enter new key: \n").encode()

		zipped = list(zip(key, arr))
	
		for i in range(arrLen):
			temp = zipped[i][0]^int(zipped[i][1])
			string += chr(temp)

		f = open("plaintext.txt", "w+")
		f.write(string)
		f.close()
		print(string)

	else:
		print("input must be \"e\" or \"d\"")

oneTimePad()

