import json
import os

FILE_NAME = "tasks_data.txt"
tasks = []
next_id = 1

def save_to_file():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
        print("💾 Tasks saved successfully.")
    except Exception as e:
        print(f"❌ Failed to save tasks: {e}")

def load_from_file():
    global tasks, next_id
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)
            if tasks:
                next_id = max(task["id"] for task in tasks) + 1
            print("📂 Tasks loaded from file.")
        except Exception as e:
            print(f"❌ Failed to load tasks: {e}")
    else:
        print("📁 No saved tasks found.")

def create_task():
    global next_id

    # Get name (not empty, max 5 words)
    while True:
        name = input("Task Name (max 5 words): ").strip()
        word_count = len(name.split())
        if not name:
            print("⚠️ Name cannot be empty!")
        elif word_count > 5:
            print(f"⚠️ Name is too long! ({word_count} words) Please use 5 words or fewer.")
        else:
            break

    # Get description (not empty, max 15 words)
    while True:
        description = input("Description (max 15 words): ").strip()
        word_count = len(description.split())
        if not description:
            print("⚠️ Description cannot be empty!")
        elif word_count > 15:
            print(f"⚠️ Description is too long! ({word_count} words) Please use 15 words or fewer.")
        else:
            break

    # Get priority
    valid_priorities = ["High", "Medium", "Low"]
    while True:
        priority = input("Priority (High/Medium/Low): ").capitalize()
        if priority in valid_priorities:
            break
        print("⚠️ Invalid priority! Please enter High, Medium, or Low.")

    # Get status
    valid_statuses = ["Pending", "In Progress", "Done"]
    while True:
        status = input("Status (Pending/In Progress/Done): ").title()
        if status in valid_statuses:
            break
        print("⚠️ Invalid status! Please enter Pending, In Progress, or Done.")

    task = {
        "id": next_id,
        "name": name,
        "description": description,
        "priority": priority,
        "status": status
    }

    tasks.append(task)
    print(f"✅ Task '{name}' added with ID {next_id}")
    next_id += 1
    save_to_file()

def view_tasks():
    if not tasks:
        print("❌ No tasks available!")
    else:
        print("\n📋 Task List:")
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"  Name       : {task['name']}")
            print(f"  Description: {task['description']}")
            print(f"  Priority   : {task['priority']}")
            print(f"  Status     : {task['status']}")
            print("-" * 30)

def update_task():
    if not tasks:
        print("❌ No tasks to update!")
        return

    view_tasks()
    task_id = input("Enter the ID of the task to update: ")

    if task_id.isdigit():
        task_id = int(task_id)
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            print("Leave blank to keep current value.")
            name = input(f"New Name [{task['name']}]: ") or task['name']
            description = input(f"New Description [{task['description']}]: ") or task['description']
            priority = input(f"New Priority [{task['priority']}]: ") or task['priority']
            status = input(f"New Status [{task['status']}]: ") or task['status']

            task.update({
                "name": name,
                "description": description,
                "priority": priority,
                "status": status
            })
            print("✅ Task updated!")
            save_to_file()
        else:
            print("❌ Task with that ID not found!")
    else:
        print("⚠️ Please enter a valid number!")

def delete_task():
    if not tasks:
        print("❌ No tasks to delete!")
        return

    view_tasks()
    task_id = input("Enter the ID of the task to delete: ")

    if task_id.isdigit():
        task_id = int(task_id)
        index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)
        if index is not None:
            deleted_task = tasks.pop(index)
            print(f"🗑️ Deleted task '{deleted_task['name']}' (ID {deleted_task['id']})")
            save_to_file()
        else:
            print("❌ Task with that ID not found!")
    else:
        print("⚠️ Please enter a valid number!")

def search_tasks():
    if not tasks:
        print("❌ No tasks available to search!")
        return

    keyword = input("🔍 Enter keyword to search (name or description): ").strip().lower()
    if not keyword:
        print("⚠️ Please enter a valid keyword!")
        return

    matches = [
        task for task in tasks
        if keyword in task['name'].lower() or keyword in task['description'].lower()
    ]

    if matches:
        print(f"\n🔎 Found {len(matches)} matching task(s):")
        for task in matches:
            print(f"ID: {task['id']}")
            print(f"  Name       : {task['name']}")
            print(f"  Description: {task['description']}")
            print(f"  Priority   : {task['priority']}")
            print(f"  Status     : {task['status']}")
            print("-" * 30)
    else:
        print("❌ No tasks matched your keyword.")

def main():
    load_from_file()
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
            create_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_tasks()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option! Try again.")

if __name__ == "__main__":
    main()
