alphabet = 'abcdefghijklmnopqrstuvwxyz'

text = input("Enter text to encrypt: ").strip().lower()
key = int(input("Enter key: ").strip()) % 26

result = ''
for char in text:
    if char in alphabet:
        result += alphabet[(alphabet.index(char) + key) % 26]
    else:
        result += char

print("Encrypted text:", result)
