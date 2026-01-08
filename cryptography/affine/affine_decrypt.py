def mod_inverse(a, m):
    return next((i for i in range(1, m) if (a * i) % m == 1), None)

def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Invalid 'a', choose another."
    return "".join(chr(((a_inv * ((ord(c) - 65) - b)) % 26) + 65) if c.isalpha() else c for c in text.upper())

a = int(input("Enter a: "))
b = int(input("Enter b: "))
cipher = input("Enter encrypted text: ")
print("Decrypted:", affine_decrypt(cipher, a, b))
