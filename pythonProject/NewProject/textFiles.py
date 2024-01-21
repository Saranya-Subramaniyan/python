file = open("todos.txt",'w')# overwrite
file.writelines(['hello everyone...adtygvhkjlmdxcgfbhj\n',' dfgbhnj'])
file.write("fvghjkm")

file = open("todos.txt",'r')# overwrite
todos=file.readlines()
print(todos)
# new_todos = []
# for item in todos:
#     new_item = item.strip('\n')
#     new_todos.append(new_item)
# print(todos)
new_todos = [item.strip('\n') for item in todos]

for index,item in enumerate(new_todos):
    row=f"{index}-{item}"
    print(row)

todo = file.read()
print("hello",todo)
for index,item in enumerate(todo):
    row=f"{index}-{item}"
    print(row)