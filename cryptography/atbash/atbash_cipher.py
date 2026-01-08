# Atbash cipher is symmetric:
# the same function is used for both encryption and decryption.


def atbash_cipher(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]
    result = ""
    
    for char in text.upper():
        if char in alphabet:
            index = alphabet.index(char)
            result += reversed_alphabet[index]
        else:
            result += char  
    return result


plain_text = input("Enter text you want to cipher: ") 
cipher_text = atbash_cipher(plain_text)
print("Cipher Text:", cipher_text)
