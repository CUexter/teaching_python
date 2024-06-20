from list import TodoList

def display_menu():
    print("Todo List Application")
    print("1. View Todo List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Save and Exit")

def main():
    todo_list = TodoList()

    # Load items from file if it exists
    try:
        with open("todo_list.txt", "r") as file:
            for line in file:
                todo_list.add_item(line.strip())
    except FileNotFoundError:
        pass

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            todo_list.view_items()
        elif choice == "2":
            item_description = input("Enter a new todo item: ")
            todo_list.add_item(item_description)
        elif choice == "3":
            try:
                item_number = int(input("Enter the number of the item to remove: ")) - 1
                todo_list.remove_item(item_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
