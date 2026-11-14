import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8 characters.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters (A-Z)")
        print("2. Lowercase letters (a-z)")
        print("3. Numbers (0-9)")
        print("4. Symbols (!@#$%^&*)")

        choices = input("Enter your choices (example: 1234): ")

        valid_choices = set("1234")
        selected = set(choices)

        if not selected.issubset(valid_choices):
            print("Error: Please choose only 1, 2, 3, or 4.")
            continue

        if len(selected) < 2:
            print("Error: Select at least 2 character types.")
            continue

        characters = ""

        if "1" in selected:
            characters += string.ascii_uppercase

        if "2" in selected:
            characters += string.ascii_lowercase

        if "3" in selected:
            characters += string.digits

        if "4" in selected:
            characters += string.punctuation

        password = []

        if "1" in selected:
            password.append(random.choice(string.ascii_uppercase))

        if "2" in selected:
            password.append(random.choice(string.ascii_lowercase))

        if "3" in selected:
            password.append(random.choice(string.digits))

        if "4" in selected:
            password.append(random.choice(string.punctuation))

        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)

        print("\n===== GENERATED PASSWORD =====")
        print(password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")
