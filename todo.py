def show_tasks():
    pass
def add_task():
    pass
def delete_task():
    pass
def mark_done():
    pass

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No task found.")
                return
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(f"{task} | Not Done\n")
    print("Task added.")

def delete_task(task_number):
    with open("task.txt", "r") as file:
        tasks = file.readlines()
    if 0 < task_number <= len(tasks):
        del tasks[task_number-1]
        with open("task.txt", "w") as file:
            file.writelines(tasks)
        print("Task Deleted.")
    else:
        print("Invalid task number.")

def mark_done(task_number):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 0 < task_number <= len(tasks):
        task_pasts = tasks[task_number - 1]. strip.split(" |  ")
        task_parts[1] = "Done"
        tasks[task_number - 1] = "|".join(task_parts) + "\n"
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as done.")
    else:
        print("Invalid Task number.")



def main():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "i":
            show_tasks()
        elif choice == "2":
            task = input("Enter task:")
            add_task(task)
        elif choice == "3":
            show_tasks()
            task_number = int(input("Enter task number to mark as done."))
            mark_done(task_number)
        elif choice == "4":
            show_tasks()
            task_number = int(input("Enter task number to deleted."))
            delete_task(task_number)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try Again.")

if __name__ == "_main_":
    main()

