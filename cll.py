#from functions import open_file, write_todos
import functions as funct
import time

now = time.strftime("%d/%m/%Y %H:%M:%S")
print("It is", now)

while True:
    # get user input and strip space characters
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        # older version: todo = input("Enter a to do: ") + "\n"
        # new version, the to-do is whatever the user wrote after "add "
        todo = user_action[4:] + "\n"
        # open (create if non-existent) a txt file.
        # file = open('todos.txt', 'r')
        # todos = file.readlines()as
        # file.close()

        # better with the following (no need to close files):
        # with open('todos.txt', 'r') as file:
        #    todos = file.readlines()

        todos = funct.open_file()

        todos.append(todo)

        #with open('todos.txt', 'w') as file:
        #    file.writelines(todos)
        funct.write_todos(todos)
# keeping just one "if" makes the program faster, as the other "if"s are not executed unless the first iff is not matched.

    elif user_action.startswith("show"):
        todos = funct.open_file()

        # Remove list backspace and leave only the default backspace the for method has:
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)
        # it's better with list comprehension:
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            #remove backspace with the simplest solution:
            item = item.strip("\n")
            row = f"{index+1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            # older version:  number = int(input("Number of the to-do you want to edit: "))-1
            number = int(user_action[5:])-1

            todos = funct.open_file()

            new_todo = input("Enter new to-do: ")
            todos[number] = new_todo + "\n"

            funct.write_todos(todos)
        except ValueError:
            print("Your command is wrong.")
            continue
            #runs another cycle of the while loop

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])-1

            todos = funct.open_file()

            to_be_removed = todos[number].strip("\n")
            todos.pop(number)

            funct.write_todos(todos)

            print(f"{to_be_removed} was removed from the list.")
        except IndexError:
            print(f"There's no item with number {number+1}")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Wrong command")

print("Bye!")