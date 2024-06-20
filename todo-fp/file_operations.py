def load_from_file(filename="todo_list.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_to_file(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for item in todo_list:
            file.write(item + "\n")
    print("Todo list saved.")
