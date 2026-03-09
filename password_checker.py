import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Uppercase check
    if re.search("[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.\n"

    # Number check
    if re.search("[0-9]", password):
        strength += 1
    else:
        remarks += "Add at least one number.\n"

    # Special character check
    if re.search("[@#$%^&*!]", password):
        strength += 1
    else:
        remarks += "Add at least one special character (@#$%^&*!).\n"

    # Strength result
    if strength == 4:
        result = "Strong Password 💪"
    elif strength == 3:
        result = "Medium Password 🙂"
    else:
        result = "Weak Password ⚠️"

    return result, remarks


password = input("Enter your password: ")
result, remarks = check_password_strength(password)

print("\nPassword Strength:", result)

if remarks:
    print("Suggestions:")
    print(remarks)