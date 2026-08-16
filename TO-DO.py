import json
import os

FILENAME = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except Exception:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks list
def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\n--- YOUR TO-DO LIST ---")
    for index, task in enumerate(tasks, 1):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print("Task added successfully!")
        list_tasks(tasks)
    else:
        print("Task cannot be empty!")

# Mark task as completed
def mark_done(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
            list_tasks(tasks)
        else:
            print("Error: Invalid task number!")
    except ValueError:
        print("Error: Please enter a valid number!")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted task: '{removed['title']}'")
            list_tasks(tasks)
        else:
            print("Error: Task number does not exist!")
    except ValueError:
        print("Error: Please enter a valid number!")

# Main menu loop
def main():
    tasks = load_tasks()
    while True:
        print("\n=====================")
        print("TO-DO LIST APP")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting app. Goodbye bro!")
            break
        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()