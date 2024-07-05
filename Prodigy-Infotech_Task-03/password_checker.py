import re

def check_password_complexity(password):
    if len(password) < 8:
        return "Password too short! Must be at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return "Password is strong."

if __name__ == "__main__":
    password = input("Enter a password to check its complexity: ")
    result = check_password_complexity(password)
    print(result)

