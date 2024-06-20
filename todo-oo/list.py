from item import TodoItem

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item_description):
        item = TodoItem(item_description)
        self.items.append(item)
        print(f"'{item_description}' has been added to your todo list.")

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            print(f"'{removed}' has been removed from your todo list.")
        else:
            print("Invalid item number.")

    def view_items(self):
        if not self.items:
            print("Todo list is empty.")
        else:
            for idx, item in enumerate(self.items, 1):
                print(f"{idx}. {item}")

    def save_to_file(self, filename="todo_list.txt"):
        with open(filename, "w") as file:
            for item in self.items:
                file.write(str(item) + "\n")
        print("Todo list saved.")
