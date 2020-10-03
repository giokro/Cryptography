from pytea import TEA
import os

key = os.urandom(16)
print('key is', key)

string = "So what we smoke weed\nWe're just having fun\nWe don't care who sees"

tea = TEA(key)

ciphertext = tea.encrypt(string.encode())
print(ciphertext)

plaintext = tea.decrypt(ciphertext).decode()
print(plaintext)






