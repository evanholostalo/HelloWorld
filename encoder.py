#Evan Ho Lostalo
def encode(password):
    encoded = ''
    for char in password:
        encoded += str((int(char) + 3) % 10)  # Shift the digit up by 3 and handle wrap-around
    return encoded


def main():
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif choice == "2":
            print("Decoder function not implemented yet.")

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()