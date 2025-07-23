# todo.py

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def delete_task(index):
    try:
        removed = todo_list.pop(index - 1)
        print(f"Deleted task: {removed}")
    except IndexError:
        print("Invalid task number.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
