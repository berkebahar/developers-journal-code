def decimal_to_binary(n):
    binary = bin(n)[2:]  
    return binary.zfill(8)  

def text_to_binary(text):
    binary_text = []
    for char in text:
        ascii_value = ord(char)  # Get the ASCII value of the character
        binary_char = decimal_to_binary(ascii_value)  # Convert ASCII to binary
        binary_text.append(binary_char)
    return ' '.join(binary_text)

plain_text = input("Enter the text you want to cipher: ")
cipher_text = text_to_binary(plain_text)
print("Encrypted Text (Binary):", cipher_text)
