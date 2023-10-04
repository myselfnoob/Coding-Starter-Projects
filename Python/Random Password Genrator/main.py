import secrets
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    secure_password = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print("Generated Password: " + password)

if __name__ == "__main__":
    main()
