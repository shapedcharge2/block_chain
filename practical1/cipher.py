def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)  # Decryption is just negative shift for encryption

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice == 'e':
        plaintext = input("Enter the plaintext: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_encrypt(plaintext, shift)
        print("Encrypted text:", encrypted_text)
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()

