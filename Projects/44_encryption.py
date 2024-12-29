import string
import random

chars = list(" " + string.punctuation + string.ascii_letters + string.digits)
key = chars.copy()

random.shuffle(key)

usr = input("Enter a message to encrypt: ")
en_msg = ""

# ENCRYPT
for character in usr:
    index = chars.index(character)
    en_msg += key[index]

print(f"Original message: {usr}")
print(f"Encrypted message: {en_msg}")
