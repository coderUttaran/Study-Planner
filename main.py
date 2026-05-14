import json


def load_data():
    with open("data.json") as file:
        data = json.load(file)
        return data
    
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)



def add_tasks():
    data = load_data()
    print()

    task_name = input("Enter task name: ")
    subject = input("Enter Subject name: ")
    deadline = input("Enter the deadline: ")

    task = {
        "task" : task_name,
        "subject" : subject,
        "deadline" : deadline,
        "status" : "pending"
    }

    data.append(task)
    save_data(data)
    print()
    print("Task added")
    print()


def view_tasks():
    data = load_data()
    print()

    if data:

        for i, task in enumerate(data):
            print(f"Task {i+1}.")

            for key, value in task.items():
                print(f"\t{key} : {value}")
        
        print()
        
    else:
        print("There are no tasks")
        print()
        return -1


def mark_tasks():
    data = load_data()
    view_tasks()
    print()
    if view_tasks() == -1:
        print()
        return
    print()

    try:
        
        ind = int(input("Enter task no. to mark complete: "))
        ind -= 1
        if data[ind]["status"] == "Completed":
            print()
            print("Task already completed")
            print()
        else:

            data[ind]["status"] = "Completed"
            save_data(data)
            print()
            print("Task Completed!")
            print()

            for key, value in data[ind].items():
                print(f"\t{key} : {value}")
            print()

    except IndexError:
        print()
        print(f"There is no Task having no. {ind+1}")
        print()
    except ValueError:
        print()
        print("Invalid Input")
        print()


def delete_tasks():
    data = load_data()
    print()
    view_tasks()
    if view_tasks() == -1:
        print()
        return
    print()

    try:
        
        print()
        ind = int(input("Enter the task no. to delete: "))
        ind-=1

        del data[ind]
        print()
        print("Task deleted successfully")
        print()

        save_data(data)

    except ValueError:
        print()
        print("Invalid Input")
        print()
    except IndentationError:
        print()
        print(f"There is no task having task no. {ind+1}")
        print()


def main():
    while True:
        print("Student Study Planner")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark Complete")
        print("4. Delete task")
        print("5. Exit")

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
                delete_tasks()
            elif choice == 5:
                print()
                print("Thank you")
                print("Exiting...")
                break
            else:
                print("Invalid Choice")

        except ValueError:
            print()
            print("Invalid Input")
            print()

main()
