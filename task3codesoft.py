'''A password generator is a useful tool that generates strong and

random passwords for users. This project aims to create a
password generator application using Python, allowing users to

specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the

password.

Generate Password: Use a combination of random characters to

generate a password of the specified length. '''
import random                                           
import string

def  password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print(" enter a  number.")
            else:
                break
        except ValueError:
            print("SPlease enter a valid integer.")

    # Generate and display the password
    password = password_generate(length)
    print(f"\npassword: {password}")

if __name__ == "__main__":
    main()
