from datetime import datetime
import hashlib
import os

"""
Single string hash:

MD5: 1 - 0:00:00.000042; 2 - 0:00:00.000041; 3 - 0:00:00.000052; 4 - 0:00:00.000043; 5 - 0:00:00.000045; avg = 0:00:00.000044.6;

SHA-1: 1 - 0:00:00.000059; 2 - 0:00:00.000043; 3 - 0:00:00.000059; 4 - 0:00:00.000059; 5 - 0:00:00.000052; avg = 0:00:00.000054.4;

SHA-256: 1 - 0:00:00.000042; 2 - 0:00:00.000068; 3 - 0:00:00.000053; 4 - 0:00:00.000057; 5 - 0:00:00.000059; avg = 0:00:00.000055.8;


Multiple string hash:

MD5: 1 - 0:00:00.000076; 2 - 0:00:00.000056; 3 - 0:00:00.000101; 4 - 0:00:00.000075; 5 - 0:00:00.000070; avg = 0:00:00.000075.6;

SHA-1: 1 - 0:00:00.000083; 2 - 0:00:00.000060; 3 - 0:00:00.000102; 4 - 0:00:00.000086; 5 - 0:00:00.000105; avg = 0:00:00.000087.2;

SHA-256: 1 - 0:00:00.000116; 2 - 0:00:00.000096; 3 - 0:00:00.000073; 4 - 0:00:00.000086; 5 - 0:00:00.000135; avg = 0:00:00.000101.2;

"""


def md5(string, salt=None):
	if salt == None:
		salt = os.urandom(16)

	hashed = hashlib.md5(salt + string.encode())
	return [salt, hashed.hexdigest()]


def sha1(string, salt=None):
	if salt == None:
		salt = os.urandom(16)

	hashed = hashlib.sha1(salt + string.encode())
	return [salt, hashed.hexdigest()]


def sha256(string, salt=None):
	if salt == None:
		salt = os.urandom(16)

	hashed = hashlib.sha256(salt + string.encode())
	return [salt, hashed.hexdigest()]




if __name__ == "__main__":
	which = int(input("input:\n\t1 for MD5\n\t2 for SHA-1\n\t3 for SHA-256\n\n"))

	str1 = "The great big Gela found a tiny litte fella"
	str2 = "Gelo"
	str3 = "Gela"
	
	if which == 1:
		startTime = datetime.now()

		hashed = md5(str1)

		print("Finished in", datetime.now()-startTime)
		print(hashed[1])

	elif which == 2:
		startTime = datetime.now()

		hashed = sha1(str1)

		print("Finished in", datetime.now()-startTime)
		print(hashed[1])

	elif which == 3:
		startTime = datetime.now()

		hashed = sha256(str1)

		print("Finished in", datetime.now()-startTime)
		print(hashed[1])

	else:
		print("Incorrect input")








