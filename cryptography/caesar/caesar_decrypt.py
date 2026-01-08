def caesar_decrypt(cipher_text, shift):
    result = ""
    for char in cipher_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  
    return result


cipher_text = input("Enter the Caesar cipher text: ")
shift = int(input("Enter the shift value: "))
print("Decrypted Text:", caesar_decrypt(cipher_text, shift))
