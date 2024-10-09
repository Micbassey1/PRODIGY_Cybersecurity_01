
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'encrypt':
        print("Encrypted message:", encrypt(message, shift))
    elif choice == 'decrypt':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

