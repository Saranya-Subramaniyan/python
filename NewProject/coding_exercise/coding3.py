def strength(password):
    result = {"length": False, "digit": False, "isupper": False}
    if len(password) >= 8:
        result["length"] = True
    for i in password:
        if i.isdigit():
            result["digit"] = True
        if i.isupper():
            result["isupper"] = True
    return result


Password = input("Enter a password")
result = strength(Password)
if all(result):
    print("Strong Password")
else:
    print("Weak Password")