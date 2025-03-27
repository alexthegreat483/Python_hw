import json
import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1  # This will auto-increment for each task
        self.FILE_NAME = "tasks_data.txt"
        self.load_from_file()  # Auto-load tasks on startup

    def save_to_file(self):
        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump(self.tasks, file, indent=4)
            print("💾 Tasks saved successfully.")
        except Exception as e:
            print(f"❌ Failed to save tasks: {e}")

    def load_from_file(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    self.tasks = json.load(file)
                if self.tasks:
                    self.next_id = max(task["id"] for task in self.tasks) + 1
                print("📂 Tasks loaded from file.")
            except Exception as e:
                print(f"❌ Failed to load tasks: {e}")
        else:
            print("📁 No saved tasks found.")

   

    def create_task(self):
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

        # Get priority (must be one of High/Medium/Low)
        valid_priorities = ["High", "Medium", "Low"]
        while True:
            priority = input("Priority (High/Medium/Low): ").capitalize()
            if priority in valid_priorities:
                break
            print("⚠️ Invalid priority! Please enter High, Medium, or Low.")

        # Get status (must be one of Pending/In Progress/Done)
        valid_statuses = ["Pending", "In Progress", "Done"]
        while True:
            status = input("Status (Pending/In Progress/Done): ").title()
            if status in valid_statuses:
                break
            print("⚠️ Invalid status! Please enter Pending, In Progress, or Done.")

        task = {
            "id": self.next_id,
            "name": name,
            "description": description,
            "priority": priority,
            "status": status
        }

        self.tasks.append(task)
        print(f"✅ Task '{name}' added with ID {self.next_id}")
        self.next_id += 1
        self.save_to_file()  # Save on creation

    def view_tasks(self):
        if not self.tasks:
            print("❌ No tasks available!")
        else:
            print("\n📋 Task List:")
            for task in self.tasks:
                print(f"ID: {task['id']}")
                print(f"  Name       : {task['name']}")
                print(f"  Description: {task['description']}")
                print(f"  Priority   : {task['priority']}")
                print(f"  Status     : {task['status']}")
                print("-" * 30)

    def update_task(self):
        if not self.tasks:
            print("❌ No tasks to update!")
            return

        self.view_tasks()
        task_id = input("Enter the ID of the task to update: ")

        if task_id.isdigit():
            task_id = int(task_id)
            task = next((t for t in self.tasks if t["id"] == task_id), None)
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
                self.save_to_file()  # Save after update
            else:
                print("❌ Task with that ID not found!")
        else:
            print("⚠️ Please enter a valid number!")

    def delete_task(self):
        if not self.tasks:
            print("❌ No tasks to delete!")
            return

        self.view_tasks()
        task_id = input("Enter the ID of the task to delete: ")

        if task_id.isdigit():
            task_id = int(task_id)
            index = next((i for i, t in enumerate(self.tasks) if t["id"] == task_id), None)
            if index is not None:
                deleted_task = self.tasks.pop(index)
                print(f"🗑️ Deleted task '{deleted_task['name']}' (ID {deleted_task['id']})")
                self.save_to_file()  # Save after deletion
            else:
                print("❌ Task with that ID not found!")
        else:
            print("⚠️ Please enter a valid number!")

    def search_tasks(self):
        if not self.tasks:
            print("❌ No tasks available to search!")
            return

        keyword = input("🔍 Enter keyword to search (name or description): ").strip().lower()
        if not keyword:
            print("⚠️ Please enter a valid keyword!")
            return

        matches = [
            task for task in self.tasks
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

    def run(self):
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
                self.create_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.search_tasks()
            elif choice == "0":
                print("👋 Goodbye!")
                break
            else:
                print("❗ Invalid option! Try again.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()
