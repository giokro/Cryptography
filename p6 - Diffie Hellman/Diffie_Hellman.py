class Person:
	def __init__(self, private, public_p, public_g):
		self.private = private
		self.public_p = public_p
		self.public_g = public_g

		self.key = []

	def makePub(self):
		pub = (self.public_g**self.private) % self.public_p
		return pub

	def makeKey(self, else_pub):
		self.key = (else_pub**self.private) % self.public_p

#
p = 34 	# modulus
g = 4  	# base
#

Alice = Person(5, p, g)
Bob = Person(3, p, g)

Alice_pub = Alice.makePub()
Bob_pub = Bob.makePub()

Alice.makeKey(Bob_pub)
Bob.makeKey(Alice_pub)

print(Alice.key)
print(Bob.key)


