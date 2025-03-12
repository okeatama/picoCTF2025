subCipher = dict() # ciphertext:plaintext substitution

# assumption: plaintext in lowercase and ciphertext in UPPERCASE
guessCheese = input("Cheese to guess: ")
cheese1 = input("First cheese: ")
cheese1Cipher = input("Cipher of first cheese: ")

for index, char in enumerate(cheese1Cipher):
    # cheese1 and cheese1Cipher is equal in length since this is just a substitution cipher
    if char not in subCipher:
        subCipher[char] = cheese1[index]

# replace known substitutes
for char in guessCheese:
    if char in subCipher:
        guessCheese = guessCheese.replace(char, subCipher[char])
print(subCipher)
print(guessCheese)

cheese2 = input("Second cheese: ")
cheese2Cipher = input("Cipher of second cheese: ")

for index, char in enumerate(cheese2Cipher):
    subCipher[char] = cheese2[index]

# replace known substitutes
for char in guessCheese:
    if char in subCipher:
        guessCheese = guessCheese.replace(char, subCipher[char])

print(subCipher)
print(guessCheese)