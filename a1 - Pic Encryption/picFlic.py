filename = input("Filename you want to encode: ")
key = input("Key: ")


f = open(filename, "rb")
tempLines = f.readlines()

lines=[]

for i in tempLines:
	lines.append(str(i.hex()))


def hexSep(arr): # this seperates the hex from the picture, transfers it to ints and stores it in an array
	
	sepArr = []
	
	for i in arr:
		index=0
		while(True):
			if index<=len(i)-1:
				sepArr.append(int(i[index]+i[index+1],16))
				index+=2
			else: 
				break

	return sepArr


def xOr(arr, key):
	newArr = []
	
	for i in range(len(arr)):
		a = arr[i]
		b = ord(key[i%len(key)])

		newArr.append(a^b)

	return newArr


arr = hexSep(lines)

xArr = xOr(arr, key)

bArr = bytes(xArr)


# This is for adding the correct extension

outfile = "X."
ext = ""

for i in range(len(filename)):
	if filename[-1-i] == ".":
		break
	else:
		ext += filename[-1-i]

for i in range(len(ext)):
	outfile += ext[-1-i]


nf = open(outfile, "wb")
nf.write(bArr)

