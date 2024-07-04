def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) - shift_amount
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
                decrypted_text += chr(char_code)
            elif char.islower():
                if char_code < ord('a'):
                    char_code += 26
                decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == '2':
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

