import string
import random
import sys

print("""

        Random Password Generator
              v0.0.1

        -- by Sayak
              
              """)

length = int(input("Enter your password length (e.g. 8): "))

def letters_numbers():
    total = string.ascii_letters + string.digits
    password = "".join(random.sample(total, length))
    print("")
    print("Your Password is: ", password)
    print("")

def letters_numbers_punctuations():
    total = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(total, length))
    print("")
    print("Your Password is: ", password)
    print("")
    

def main():
    while True:
        print("\nChoose your password combination: ")
        print(" 1. Letters + Numbers")
        print(" 2. Letters + Numbers + Special Symbols")
        print(" 3. Exit")

        choice = input("\nChoose an Option (e.g. 1): ")

        if choice == "1":
            letters_numbers()
        elif choice == "2":
            letters_numbers_punctuations()
        elif choice == "3":
            print("")
            print("👋 Exiting... Have a great day!")
            print("")
            sys.exit()
        else:
            print("Invalid Choice\n")

        break   

if __name__ == "__main__":
    main()