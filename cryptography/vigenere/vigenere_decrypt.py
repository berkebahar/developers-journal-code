def vigenere_decrypt(text, key):
    key = key.upper()
    text = text.upper()
    decrypted = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            decrypted += chr((ord(char) - 65 - shift + 26) % 26 + 65)
            key_index += 1
        else:
            decrypted += char
    return decrypted


ciphertext = input("Enter the encrypted text: ")
key = input("Enter the key: ")

decrypted_text = vigenere_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
