from random import randint

# For the encryption to work:
#	modulus_p must be a big prime
#	base_g must be a primitive root modulo modulus_p

class Server:
	def __init__(self, priv_k, modulus_p, base_g):
		self.priv_k = priv_k
		self.modulus_p = modulus_p
		self.base_g = base_g

	def make_pub(self):
		pub_k = (self.base_g ** self.priv_k) % self.modulus_p
		return pub_k

	def decrypt(self, ciphertext):
		plaintext = ""
	
		if(len(ciphertext) % 2 != 0):
			print("Error: Malformed ciphertext")
			return
		else:
			for i in range(0, len(ciphertext), 2):
				shared_k = (ciphertext[i] ** self.priv_k) % self.modulus_p
				
				plaintext += chr((ciphertext[i+1]*pow(shared_k, self.modulus_p-2, self.modulus_p)) % self.modulus_p) 
		
			return plaintext
		

class Client:
	def __init__(self, pub_k, modulus_p, base_g):
		self.pub_k = pub_k
		self.modulus_p = modulus_p
		self.base_g = base_g

	def encrypt(self, plaintext):
		ciphertext = []
		for i in range(len(plaintext)):
			temp_priv = randint(1, self.modulus_p-1)

			shared_k = (self.pub_k ** temp_priv) % self.modulus_p

			C1 = (self.base_g ** temp_priv) % self.modulus_p
			C2 = (ord(plaintext[i]) * shared_k) % self.modulus_p

			ciphertext.append(C1)
			ciphertext.append(C2)

		return ciphertext


Alice = Server(6, 307, 11)	# priv_k, modulus_p, base_g
Bob = Client(Alice.make_pub(), Alice.modulus_p, Alice.base_g)

ciphertext = Bob.encrypt("Get back Jack\nKeep your hands off my stack")
print(ciphertext)
print(Alice.decrypt(ciphertext))

