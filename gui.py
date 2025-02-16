import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do", key="to-do")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="to-dos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box, add_button], [list_box,edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["to-dos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["to-dos"][0]
            new_todo = values["to-do"] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["to-dos"].update(values=todos)
        case "to-dos":
            window["to-do"].update(value=values["to-dos"][0])
        case sg.WIN_CLOSED:
            break

window.close()