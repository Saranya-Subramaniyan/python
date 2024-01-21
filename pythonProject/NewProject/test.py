def greet(message):
    return message.split()[0].capitalize()+" "+message.split()[1].capitalize()
greeting= greet(message="hello everyone")
print(greeting)

def add(a,b):
    return a+b
add_two=add(1,3)
print(add_two)