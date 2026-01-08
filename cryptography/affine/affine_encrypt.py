from math import gcd

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        return "Invalid 'a', choose another."
    return "".join(chr(((a * (ord(c) - 65) + b) % 26) + 65) if c.isalpha() else c for c in text.upper())

a = int(input("Enter a: "))
b = int(input("Enter b: "))
text = input("Enter text: ")
print("Encrypted:", affine_encrypt(text, a, b))
