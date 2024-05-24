def encrypt(text, shift):
    
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char 
    
    return encrypted_text


def decrypt(text, shift):
   
    return encrypt(text, -shift)  


if __name__ == "__main__":
  
    full_name = input("Enter your full name: ")
    
    while True:
        try:
            shift = int(input("Enter the shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    encrypted_name = encrypt(full_name, shift)
    print(f"Encrypted name: {encrypted_name}")
    
    decrypted_name = decrypt(encrypted_name, shift)
    print(f"Decrypted name: {decrypted_name}")
