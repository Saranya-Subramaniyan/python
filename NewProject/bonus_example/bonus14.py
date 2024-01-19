import PySimpleGUI as pg
import if_else


label = pg.Text("Type in a to-do")
input_box = pg.InputText(tooltip="Enter todo", key="todo")
add_button = pg.Button("Add")
list_box = pg.Listbox(values=if_else.get_todos(), key= 'todos',
                      enable_events= True, size = (45, 10))
edit_button = pg.Button("Edit")

window = pg.Window("My to-do app", layout=[[label], [input_box,add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print("hello",event)
    print("values",values)
    match event:
        case "Add":
            todos = if_else.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            if_else.write_todos(todos)
        case "Edit":
            todo = values['todos']
        case pg.WIN_CLOSED:
            break

window.close()