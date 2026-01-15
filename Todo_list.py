tasks = []

def display_menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    display_menu()
    
    choice = input("Select an option(1-4): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == '2':
        # Check if there are tasks available to edit
        if tasks:
            # Display the current tasks with their indices
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            # Prompt the user to enter the index of the task to edit
            try:
                task_index = int(input("Enter task index to edit: ")) - 1
                # Check if the entered index is valid
                if 0 <= task_index < len(tasks):
                    # Prompt the user to enter a new task
                    new_task = input("Enter new task: ")
                    # Update the task at the specified index
                    tasks[task_index] = new_task
                    print("Task edited successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to edit.")

    # Option 3: Delete Task
    elif choice == '3':
        # Check if there are tasks available to delete
        if tasks:
            # Display the current tasks with their indices
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            # Prompt the user to enter the index of the task to delete
            try:
                task_index = int(input("Enter task index to delete: ")) - 1
                # Check if the entered index is valid
                if 0 <= task_index < len(tasks):
                    # Remove the task at the specified index
                    tasks.pop(task_index)
                    print("Task deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to delete.")

    # Option 4: Exit
    elif choice == '4':
        # Exit the application
        print("Exiting the application. Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select a valid option.")

