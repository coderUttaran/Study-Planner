tasks = []

def add_tasks():
    global tasks
    print()

    task_name = input("Enter task name: ")
    subject = input("Enter Subject name: ")
    deadline = input("Enter the deadline: ")

    t_dict = {
        "task" : task_name,
        "subject" : subject,
        "deadline" : deadline,
        "status" : "pending"
    }

    tasks.append(t_dict)
    print()
    print("Task added")
    print()


def view_tasks():
    global tasks
    print()

    for i, task in enumerate(tasks):
        print(f"Task {i+1}.")

        for key, value in task.items():
            print(f"\t{key} : {value}")

    print()

def mark_tasks():
    global tasks
    print()

    try:
        
        ind = int(input("Enter task no. to mark complete: "))
        ind -= 1
        tasks[ind]["status"] = "Completed"
        print("Task Completed!")

        for key, value in tasks[ind].items():
            print(f"\t{key} : {value}")
        print()

    except IndexError:
        print(f"There is no Task having no. {ind+1}")
    except ValueError:
        print()
        print("Invalid Input")
        print()


def main():
    while True:
        print("Student Study Planner")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark Complete")
        print("4. Exit")

        try:
            print()
            choice = int(input("Enter your operation: "))

            if choice == 1:
                add_tasks()
            elif choice ==  2:
                view_tasks()
            elif choice == 3:
                mark_tasks()
            elif choice == 4:
                print()
                print("Thank you")
                print("Exiting...")
                break

        except ValueError:
            print()
            print("Invalid Input")
            print()

main()
