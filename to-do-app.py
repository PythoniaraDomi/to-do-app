tasks=[]

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def listTasks():
    if not tasks:
        print("Currently the list is empty.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks ()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"'{taskToDelete}' has been deleted.")
        else:
            print(f"Task #{taskToDelete} has not been found.")
    except:
        print("Invalid input.")

def editTask():
    listTasks ()
    try:
        taskToEdit = int(input("Enter the # to edit: "))
        if taskToEdit >= 0 and taskToEdit < len(tasks):
            tasks[taskToEdit]=input("Enter new value: ")
            print(f"'{taskToEdit}' has been edited.")
        else:
            print(f"Task #{taskToEdit} has not been found.")
    except:
        print("Invalid input.")

def main ():
    print("-------------\nHello in Your-To-Do-List App!\n-------------")
    print("What would you like to do? (write capital letter to perform specific action)\n-------------")


    not_stop_working = True
    while not_stop_working:
        action = str(input("""
        To add new object: insert A
        To edit existing object: insert E
        To delete existing object: insert D
        To get the current list of task: insert L
        To exit the app: insert X
        """))

        match action:
            case "A":
                addTask()
            case "E":
                editTask ()
            case "D":
                deleteTask ()
            case "L":
                listTasks ()
            case "X":
                print("Ok, thank you for using this App, see you next time!\n-------------")
                not_stop_working = False
        print("\n-------------")


if __name__ == "__main__":
    main()

