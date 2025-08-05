import time
def to_do_list():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()] #Strip() is used to remove \n
    except FileNotFoundError:
        pass

    while True:
        print("\n Select Operation")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. View Tasks")
        print("4. EXIT")

        choice = int(input("Enter Number from 1 - 4: "))

        if choice in(1,2,3):
            if choice == 1:
                with open("tasks.txt", "w") as file:
                    task = input("Enter your Task: ").capitalize()
                    tasks.append(task)

            elif choice == 2:
                with open("tasks.txt", "w") as file:
                    task = input("Enter Task Name to remove: ").capitalize()
                    if task in tasks:
                        tasks.remove(task)
                    else:
                        print("Task not found")

            elif choice == 3:
                with open("tasks.txt", "r") as file:
                    print("\n Your To-Do List: ")
                    if not tasks:
                        print("No Tasks Available")
                    else: 
                        for i, task in enumerate(tasks, 1):
                            print(f"{i}. {task}")

        elif choice == 4:
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == "y":
                print("You choose to Exit")
                print("Thank You")
                time.sleep(3 )
                break
            else:
                print("Cancelled Exit.")
        else:
            print("Please Enter a valid Input For your Task")
to_do_list()