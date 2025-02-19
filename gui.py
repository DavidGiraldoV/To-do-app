import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do", key="to-do")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="to-dos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d/%m/%Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["to-dos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["to-dos"][0]
                new_todo = values["to-do"] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["to-dos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values["to-dos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["to-dos"].update(values=todos)
                window["to-do"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "to-dos":
            window["to-do"].update(value=values["to-dos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()