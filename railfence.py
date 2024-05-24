


def encryptRailFence(plaintext, key):
   
    plaintext = "".join(plaintext.split())


    rail = [['ph' for i in range(len(plaintext))]
            for j in range(key)] 

 
    direction_down = False
    col = 0
    row = 0
    for i in range(len(plaintext)):
      
        if (row == 0) or (row == key - 1):
            direction_down = not direction_down 

      
        rail[row][col] = plaintext[i]
        col += 1

      
        if direction_down:
            row += 1
        else:
            row -= 1

   
    ciphertext = []
    for i in range(key): 
        for j in range(len(plaintext)): 
            if rail[i][j] != 'ph':
                ciphertext.append(rail[i][j])
    return "".join(ciphertext) 


def decryptRailFence(ciphertext, key):


    rail = [['*' for i in range(len(ciphertext))]
            for j in range(key)]

 
    direction_down = None
    col = 0
    row = 0

 
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1: 
            direction_down = False


        rail[row][col] = 'mkr'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

  
    idx = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == 'mkr') and
                    (idx < len(ciphertext))):
                rail[i][j] = ciphertext[idx]
                idx += 1

   
    plaintext = []
    col = 0
    row = 0
    for i in range(len(ciphertext)):
        if row == 0: 
            direction_down = True
        if row == key - 1: 
            direction_down = False

     
        plaintext.append(rail[row][col])
        col += 1

       
        if direction_down:
            row += 1
        else:
            row -= 1
    return "".join(plaintext) 


user_input = input("\nWould you like to perform encryption or decryption?\nPlease Enter 'e' or 'd': ").lower() # In case user uses capital letters
isValid = True

if user_input not in ['e', 'd']:
    print("Invalid input, please enter 'e' for encryption or 'd' for decryption.")
    isValid = False
else:

    user_input_key = input("Enter a key to use >= 2 of type (int): ")

    try:
        key = int(user_input_key)
        if key < 2: 
            print("Please enter a key a value >= 2.")
            isValid = False
    except ValueError:
        print("Invalid key input, please enter a valid number.")
        isValid = False



if user_input == 'e' and isValid == True:
  user_input_plaintext = input("\nPlease enter the plaintext to encrypt: \n")
  ciphertext = encryptRailFence(user_input_plaintext, key)
  print("\nPlaintext (Original): " + user_input_plaintext)
  print("Ciphertext (Generated): " + ciphertext)
  print("Key Value Chosen:", key) 

elif user_input == 'd' and isValid == True: 
  user_input_ciphertext = input("\nPlease enter the ciphertext to decrypt: \n")
  plaintext = decryptRailFence(user_input_ciphertext, key) 
  print("\nCiphertext (Original): " + user_input_ciphertext) 
  print("Plaintext (Generated): " + plaintext)
  print("Key Value Chosen:", key)

else: 
  print("\nAn error has occured, please try again.\n")
