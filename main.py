from pyscript import document

def create_account(e):
    username = document.getElementById("username").value
    password = document.getElementById("password").value

    output = document.getElementById("output")
    output.innerHTML = ""

    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True

    if len(username) < 7:
        output.innerHTML = "Username must contain at least 7 characters."

    elif len(password) < 10:
        output.innerHTML = "Password must be at least 10 characters long."

    elif not has_letter:
        output.innerHTML = "Password must contain at least one letter."

    elif not has_number:
        output.innerHTML = "Password must contain at least one number."

    else:
        output.innerHTML = "Account created."
