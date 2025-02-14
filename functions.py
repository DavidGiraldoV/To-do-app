FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Opens files as a local file for manipulation
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Writes to-dos on a local file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)