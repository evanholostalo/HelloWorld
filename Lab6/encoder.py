#Evan Ho Lostalo

def encode(password):
    encoded = ''
    for char in password:
        encoded += str((int(char) + 3) % 10)  # Shift the digit up by 3 and handle wrap-around
    return encoded

def decode(pass_hold):
    print(pass_hold)
    decoded = ''
    for char in pass_hold:
        decoded += str((int(char) - 3) % 10)
    print("\nThe encoded password is", pass_hold, "and the original password is", decoded + '.')

def main():
    hold_pass = ""
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            hold_pass = encode(password)
            print("Your password has been encoded and stored!")

        elif choice == "2":
            decode(hold_pass)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()