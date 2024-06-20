from menu import display_menu
from operations import view_todo_list, add_item, remove_item
from file_operations import load_from_file, save_to_file

def main():
    todo_list = load_from_file()

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            item_description = input("Enter a new todo item: ")
            todo_list = add_item(todo_list, item_description)
        elif choice == "3":
            try:
                item_number = int(input("Enter the number of the item to remove: ")) - 1
                todo_list = remove_item(todo_list, item_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            save_to_file(todo_list)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
