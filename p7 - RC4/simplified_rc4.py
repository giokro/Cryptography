def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def xor(arr1, arr2):
	ciphertext = []
	for i in range(len(arr1)):
		c = arr1[i]^arr2[i]
		ciphertext.append(c)

	return ciphertext

def rc4(plaintext, key):
	# KSA
	## init
	arr = []
	for i in range(8):
		arr.append(i)


	## now we use the key to jumble the arr
	j = 0
	for i in range(8):
		j = (j + arr[i] + key[i%len(key)]) % 8
		swap(arr, i, j)

	
	# PRGA
	## now we generate the key stream
	stream = []
	j = 0
	for i in range(len(plaintext)):
		i = (i + 1) % 8
		j = (j + arr[i]) % 8
		swap(arr, i, j)

		index = (arr[i]+arr[j]) % 8
		stream.append(arr[index])


	## now we XOR the plaintext and the stream
	ciphertext = xor(plaintext, stream)

	return ciphertext



if __name__ == "__main__":
	print("running simplified rc4...\n")

	plaintext = [1,2,2,2]
	print("Plaintext:", plaintext)
	key = [1,2,3,6]

	ciphertext = rc4(plaintext, key)	
	print("Ciphertext:", ciphertext)

	deciphered = rc4(ciphertext, key)
	print("Deciphered:", deciphered)



