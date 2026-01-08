def vigenere_encrypt(text, key):
    key = key.upper()
    text = text.upper()
    encrypted = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            encrypted += char
    return encrypted


plaintext = input("Enter text to encrypt: ")
key = input("Enter the key: ")

ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted text:", ciphertext)
