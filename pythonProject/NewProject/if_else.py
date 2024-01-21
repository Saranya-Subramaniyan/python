integ = input("enter a number")
print(integ*2, int(integ)*2) #33 6
def get_todos():
    with open("../todos.txt", 'r') as file:
        todos = file.readlines()
    return todos
def write_todos(filepath ="../todos.txt",todos_arg=""):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
while True:
    user_action = input("Type add, show,edit, exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        try:
            number = int(user_action[5:6])
            todos = get_todos()
            todo = user_action[4:]+'\n'
            todos.append(todo)
            todo = user_action[4:9]+'\n'
            todos.append(todo)
            todo = input("enter a todo: ")+'\n'
            todos.append(todo)
            # with open("todos.txt", 'w') as file:
            #     file.writelines(todos)
            write_todos("todos.txt",todos)
        except ValueError:
             print("Your command not valid")
             continue
    elif 'show' in user_action:
        todos=get_todos()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    else:
        exit()