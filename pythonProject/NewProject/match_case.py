
todos = []

while True:
    user_action = input("type add or show :").strip()

    match user_action:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo);
        case 'show' | 'display':
            # print(todos)
            for item in todos:
                item =item.title() # 1st letter capital
                print(item)
        case 'edit':
            number = int(input("number of the todo to edit: "))
            print(type(number))
            number = number - 1
            existing_todo = todos[number]
            new_todo = input("eneter a new todo")
            todos[number] = new_todo
            print("got it!!", existing_todo)
        case 'complete':
            number = int(input("number of the todo to complete:"))
            todos.pop(number) # remove index number
        case 'exit':
            break
        case _: # case whatever:
            print("enter a valid action")
print("byee")

for c in 'meals':
    print(c.capitalize())