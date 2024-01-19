password = input ("enter a password")

result = {}

length_password = False

if len(password)>=8:
    result["length"] = True
else:
    result["length"] = False

isdigit = False
for i in password:
    if i.isdigit():
        isdigit= True
result["digit"] = isdigit
is_upper = False
for i in password:
    if i.isupper():
        is_upper= True
result["upper"] = is_upper

print(result)
if all(result.values()):
    print("Strong password")
else:
    print("Weak Password")
