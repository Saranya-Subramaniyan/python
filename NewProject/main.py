# print("enter a todo:")
prompt = "enter a todo"
user_text = input(prompt)
user_text2 = input(prompt)
user_text3 = input(prompt)
print("user text", user_text )
length = len(user_text)
todos = [user_text, user_text2, user_text3, "hello"]
print(todos)
print(type(prompt), type(user_text), type(todos) , length)

todos = [] #empty list
while True:
       todo1 = input(prompt)
       todos.append(todo1)
       print(todos)