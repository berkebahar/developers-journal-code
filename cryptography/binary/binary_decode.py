def binary_to_decimal(binary):
    return int(binary, 2)  # Convert binary string to decimal

def binary_to_text(binary_text):
    binary_values = binary_text.split()  # Split the binary text into individual binary values
    text = ''.join(chr(binary_to_decimal(bv)) for bv in binary_values)  # Convert each binary to a character
    return text

cipher_text = input("Enter the binary text to decrypt: ")
plain_text = binary_to_text(cipher_text)
print("Decrypted Text:", plain_text)
