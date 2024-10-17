task=[]
tasks=[]
filtered=[]

def addTask():
    task = [input("Enter a task: "),
            input("Enter a date: "),
            input("Enter a duration time in minutes: "),
            input("Enter a category: "),
            input("Enter additional notes: ")]
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def listTasks():
    if not tasks:
        print("Currently the list is empty.")
    else:
        print("Current tasks:")
        for (index, task) in enumerate(tasks):
            print(f"Task #{index}. {task}")

def filterTasks(): #how to insert category
    category = (input("Enter a category you would like to filter by: "))
    if category in tasks:
        filtered = list(filter(lambda x: x[3] == category, tasks))
        print(f"Currently in '{category}' category there are following tasks:")
        for (index, task) in enumerate(filtered):
                print(f"Task #{index}. {task}.")
    else:
        print(f"'{category}' category not found.")

def dateFormat(): #temporary function, on hold
    from datetime import datetime
    date_str = tasks[1][1]
    date_object = datetime.strptime(date_str, '%d.%m.%Y').date()
    print(date_object)


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
            tasks[taskToEdit]=[ input("Enter new value for task or type 'no change': "),
                                input("Enter new value for date: "),
                                input("Enter new value for duration time in minutes: "),
                                input("Enter new value for category: "),
                                input("Enter new value for additional notes: ")]
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
        To filter tasks per category: insert F
        To get dates: insert I
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
            case "F":
                filterTasks ()
            case "X":
                print("Ok, thank you for using this App, see you next time!\n-------------")
                not_stop_working = False
                print("\n-------------")
            case "I": #temporary
                dateFormat ()
            case _:
                print("Invalid input. Please try again.")



if __name__ == "__main__":
    main()

