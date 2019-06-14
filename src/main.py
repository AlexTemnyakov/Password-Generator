import random


def generate_password(length):
    password = ""
    for i in range(length):
        # from 33 because all symbols before from 0 to 32 are not visible, 127 is not visible
        password += chr(random.randint(33, 127))
    return password


def save_passwords(listOfPasswords):
    with open("passwords.txt", "w", encoding="utf-8") as file:
        i = 1
        for password in listOfPasswords:
            file.write(str(i) + ". Password: " + password + "\n")
            i += 1


if __name__ == "__main__":
    length = int(input("Enter password length "))
    numOfPasswords = int(input("Enter the number of passwords you want to generate "))
    listOfPasswords = []
    for i in range(numOfPasswords):
        listOfPasswords.append(generate_password(length))
    save_passwords(listOfPasswords)

