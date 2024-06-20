def view_todo_list(todo_list):
    if not todo_list:
        print("Todo list is empty.")
    else:
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")

def add_item(todo_list, item_description):
    return todo_list + [item_description]

def remove_item(todo_list, index):
    if 0 <= index < len(todo_list):
        return todo_list[:index] + todo_list[index+1:]
    else:
        print("Invalid item number.")
        return todo_list
