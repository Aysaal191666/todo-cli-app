# To-Do CLI App\n
# todo.py

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

if __name__ == "__main__":
    task = input("Enter a task: ")
    add_task(task)
