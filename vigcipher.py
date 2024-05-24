def encrypt(text, key):
   
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - 65
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    
    return encrypted_text


def decrypt(text, key):
   
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - 65
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    
    return decrypted_text


if __name__ == "__main__":
    # Ask the user for their full name
    full_name = input("Enter your full name: ")
    
    # Ask the user for the key
    key = input("Enter the key: ")
    
    encrypted_name = encrypt(full_name, key)
    print(f"Encrypted name: {encrypted_name}")
    
    decrypted_name = decrypt(encrypted_name, key)
    print(f"Decrypted name: {decrypted_name}")
