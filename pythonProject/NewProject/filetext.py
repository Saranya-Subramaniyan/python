file = open("todos.txt",'r')
todos = file.readlines()
print(todos)
file.close()

with open('todos.txt', 'r') as file:
    todos = file.readlines()
print(todos)

todos = "edrftgyhuji"

with open('todos.txt', 'w') as file:
    file.writelines(["azsxdcfvgbh\n","dxcfvgbhnjmk\n",todos])
