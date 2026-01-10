def encrypt_character(character, shift1, shift2):
    # ASCII values for 'a' and 'A'
    a = ord('a')
    A = ord('A')
    if character.islower():
        # current position of our character from lowercase 'a'
        position = ord(character) - a
        if character <= 'm':
            position += shift1 * shift2
        else:
            position -= shift1 + shift2
        
        # to have the position stay between the range 0-25
        position = position % 26
        shifted_character = chr(a + position)
    
    elif character.isupper():
        # current position of our character from lowercase 'A'
        position = ord(character) - A
        if character <= 'M':
            position -= shift1
        else:
            position += shift2 ** 2
        position = position % 26
        shifted_character = chr(A + position)

    else:
        # ignore non alphabetical characters
        shifted_character = character 
    
    return shifted_character

def decrypt_character(character, shift1, shift2):
    # ASCII values for 'a' and 'A'
    a = ord('a')
    A = ord('A')
    
    if character.islower():
        # current position of our character from lowercase 'a'
        position = ord(character) - a
        if character <= 'm':
            # reverse: was shifted forward, so shift backward
            position -= shift1 * shift2
        else:
            # reverse: was shifted backward, so shift forward
            position += shift1 + shift2
        
        # to have the position stay between the range 0-25
        position = position % 26
        decrypted_character = chr(a + position)
    
    elif character.isupper():
        # current position of our character from uppercase 'A'
        position = ord(character) - A
        if character <= 'M':
            # reverse: was shifted backward, so shift forward
            position += shift1
        else:
            # reverse: was shifted forward, so shift backward
            position -= shift2 ** 2
        
        position = position % 26
        decrypted_character = chr(A + position)
    else:
        decrypted_character = character 
    
    return decrypted_character

def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r") as f:
        file_contents = f.read()

    encrypted =  ""

    for character in file_contents:
        encrypted += encrypt_character(character, shift1, shift2)

    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)

def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt","r") as f:
        file_contents = f.read()

    decrypted = ""

    for character in file_contents:
        decrypted += decrypt_character(character, shift1, shift2)

    with open("decrypted_text.txt","w") as f:
        f.write(decrypted)

def verify_decryption():
    with open("raw_text.txt", "r") as f1:
        original = f1.read()

    with open("decrypted_text.txt", "r") as f2:
        decrypted = f2.read()

    if original == decrypted:
        print("Decryption is succesfull")
    else:
        print("Decryption failed")
        

def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1=shift1, shift2=shift2)
    decrypt_file(shift1=shift1, shift2=shift2)
    verify_decryption()

main()