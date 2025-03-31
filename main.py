FILE_NAME = "tasks_data.txt"

def save_to_file(tasks):
    with open(FILE_NAME, "w") as file:
        file.write(str(tasks))
    print("Tasks saved successfully.")

def load_from_file():
    tasks = []
    next_id = 1
    try_file = open(FILE_NAME, "r")
    content = try_file.read()
    try_file.close()
    if content.strip():
        tasks = eval(content)  
        next_id = max(task["id"] for task in tasks) + 1
        print("Tasks loaded from file.")
    else:
        print("No tasks found in file.")
    return tasks, next_id

def create_task(tasks, next_id):
    while True:
        name = input("Task Name (max 5 words): ").strip()
        if not name:
            print("Name cannot be empty!")
        elif len(name.split()) > 5:
            print(f"Name is too long! ({len(name.split())} words) Please use 5 or fewer.")
        else:
            break

    while True:
        description = input("Description (max 15 words): ").strip()
        if not description:
            print("Description cannot be empty!")
        elif len(description.split()) > 15:
            print(f"Description is too long! ({len(description.split())} words) Please use 15 or fewer.")
        else:
            break

    valid_priorities = ["High", "Medium", "Low"]
    while True:
        priority = input("Priority (High/Medium/Low): ").capitalize()
        if priority in valid_priorities:
            break
        print("Invalid priority! Please enter High, Medium, or Low.")

    valid_statuses = ["Pending", "In Progress", "Done"]
    while True:
        status = input("Status (Pending/In Progress/Done): ").title()
        if status in valid_statuses:
            break
        print("Invalid status! Please enter Pending, In Progress, or Done.")

    task = {
        "id": next_id,
        "name": name,
        "description": description,
        "priority": priority,
        "status": status
    }

    tasks.append(task)
    print(f"Task '{name}' added with ID {next_id}")
    save_to_file(tasks)
    return tasks, next_id + 1

def view_tasks(tasks):
    if not tasks:
        print(" No tasks available!")
    else:
        print("\n Task List:")
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"  Name       : {task['name']}")
            print(f"  Description: {task['description']}")
            print(f"  Priority   : {task['priority']}")
            print(f"  Status     : {task['status']}")
            print("-" * 30)

def update_task(tasks):
    if not tasks:
        print(" No tasks to update!")
        return tasks

    view_tasks(tasks)
    task_id = input("Enter the ID of the task to update: ")

    if task_id.isdigit():
        task_id = int(task_id)
        taskFound = False
        for task in tasks:
            if task["id"] == task_id:
                taskFound = True
                print("Leave blank to keep current value.")
                name = input(f"New Name [{task['name']}]: ") or task['name']
                description = input(f"New Description [{task['description']}]: ") or task['description']
       
                valid_priorities = ["High", "Medium", "Low"]
                while True:
                    priority = input("Priority (High/Medium/Low): ").capitalize()
                    if priority in valid_priorities:
                        break
                    print("Invalid priority! Please enter High, Medium, or Low.")
        
                valid_statuses = ["Pending", "In Progress", "Done"]
                while True:
                    status = input("Status (Pending/In Progress/Done): ").title()
                    if status in valid_statuses:
                        break
                    print("Invalid status! Please enter Pending, In Progress, or Done.")

                task.update({
                    "name": name,
                    "description": description,
                    "priority": priority,
                    "status": status
                })
                print("Task updated!")
                save_to_file(tasks)
            
        if taskFound == False:
            print("Task with that ID not found!")
            return tasks
    else:
        print("Please enter a valid number!")
    return tasks

def delete_task(tasks):
    if not tasks:
        print(" No tasks to delete!")
        return tasks

    view_tasks(tasks)
    task_id = input("Enter the ID of the task to delete: ")

    if task_id.isdigit():
        task_id = int(task_id)
        for i in range(len(tasks)):
            if tasks[i]["id"] == task_id:
                deleted_task = tasks.pop(i)
                print(f"Deleted task '{deleted_task['name']}' (ID {deleted_task['id']})")
                save_to_file(tasks)
                return tasks
        print("Task with that ID not found!")
    else:
        print("Please enter a valid number!")
    return tasks

def search_tasks(tasks):
    if not tasks:
        print("No tasks available to search!")
        return

    keyword = input("Enter keyword to search (name or description): ").strip().lower()
    if not keyword:
        print("Please enter a valid keyword!")
        return

    matches = []
    for task in tasks:
        if keyword in task['name'].lower() or keyword in task['description'].lower():
            matches.append(task)

    if matches:
        print(f"\nFound {len(matches)} matching task(s):")
        for task in matches:
            print(f"ID: {task['id']}")
            print(f"  Name       : {task['name']}")
            print(f"  Description: {task['description']}")
            print(f"  Priority   : {task['priority']}")
            print(f"  Status     : {task['status']}")
            print("-" * 30)
    else:
        print("No tasks matched your keyword.")

def main():
    tasks, next_id = load_from_file()
    while True:
        print("\n===== Task Manager =====")
        print("1 - Create a new task")
        print("2 - View tasks")
        print("3 - Update task")
        print("4 - Delete task")
        print("5 - Search tasks")
        print("0 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            tasks, next_id = create_task(tasks, next_id)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            tasks = update_task(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
