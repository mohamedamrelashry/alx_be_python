def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
         if not(choice.isdigit() and 1 <= int(choice) <= 4):
            print("Invalid input. Please enter a number between 1 and 4.")
            display_menu()

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            item = input("What item do you want to remove ? ")
            shopping_list.remove(item)
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
