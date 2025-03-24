# homework task
tasks = []
# this make new tasks
def create_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")
# this will show there are no tasks available
def view_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("\n📋 Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
# this allows u to update a present task and add what u want to it or remove
def update_task():
    view_tasks()
    try:
        num = int(input("Enter task number to update: ")) - 1
        if 0 <= num < len(tasks):
            new_task = input("Enter the new task: ")
            tasks[num] = new_task
            print("Task updated!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")
# simle, deletes a task that u dont want
def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            print(f"Deleted: {tasks.pop(num)}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\n1 - Create a new task")
    print("2 - View tasks")
    print("3 - Update task")
    print("4 - Delete task")
    print("0 - Exit the program")
    
    choice = input("Choose an option: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option! Try again.")