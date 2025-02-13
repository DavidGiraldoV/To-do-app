import functions
import FreeSimpleGUI as FSG

label = FSG.Text("Type in a to-do:")
input_box = FSG.InputText(tooltip="Enter to-do")
add_button = FSG.Button("Add")

window = FSG.Window("My To-Do App", layout=[[label],[input_box, add_button]])
window.read()
window.close()