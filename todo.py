while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")

        with open("todos.txt", "a") as file:
            file.write(task + "\n")

        print("Task added!")

    elif choice == "2":
        try:
            with open("todos.txt", "r") as file:
                tasks = file.readlines()

            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

        except FileNotFoundError:
            print("No tasks found.")

    elif choice == "3":
        try:
            with open("todos.txt", "r") as file:
                tasks = file.readlines()

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

            task_num = int(input("Enter task number to mark done: "))

            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = "[DONE] " + tasks[task_num - 1]

                with open("todos.txt", "w") as file:
                    file.writelines(tasks)

                print("Task marked done!")
            else:
                print("Invalid task number.")

        except FileNotFoundError:
            print("No tasks found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")