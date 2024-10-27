task=[]
tasks=[]
filtered=[]

todayTasks = []
weekTasks = []
monthTasks = []

import datetime
from datetime import datetime, timedelta

import pandas as pd

current_date = datetime.now().date()
week_from_now = current_date + timedelta(weeks=1)
month_from_now = current_date + timedelta(days=30)

def addTask():
    print("\n-------------")
    task = [input("Enter a task: "),
            input("Enter a date [expected format: DD.MM.YYYY]: ")]

    original_date = task[1]
    task_date = datetime.strptime(original_date, '%d.%m.%Y').date()
    if task_date < current_date:
        print(f"Are you sure that you want to add task from the past to the list?")
        confirmation = input("Type: Yes or No\n")
        if confirmation != "Yes":
            print(f"Thanks for the confirmation. The task hasn't been added to the list.")
        else:
            print(f"'Thanks for the confirmation. Please continue")
    task.append(int(input("Enter a duration time in minutes: ")))
    task.append(input("Enter a category: "))
    task.append(input("Enter additional notes: "))
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def listTasks():
    print("\n-------------")
    if not tasks:
        print("Currently the list is empty.")
    else:
        print("Current tasks:\n")
        for (index, task) in enumerate(tasks):
            print(f"Task #{index+1}. {task}")

def filterCategory():
    print("\n-------------")
    category = [sublist[3] for sublist in tasks]
    unique_categories = list(set(category))
    print(f"Currently on your list there are tasks in the following categories:")
    for (index, element) in enumerate(unique_categories):
        print(f"#{index+1}.{element}")
    print("-------------\n")

    applied_filter = input("What category do you want filter by?\n")
    if applied_filter in category:
        filtered = list(filter(lambda x: x[3] == applied_filter, tasks))
        print(f"Currently in '{applied_filter}' category there are following tasks:")
        for (index, task) in enumerate(filtered):
            print(f"Task #{index+1}. {task}.")
    else:
        print(f"'{applied_filter}' category not found.")


def filterDate():
    not_stop_working = True
    while not_stop_working:
        action = str(input("""
        To filter pending tasks for today: insert T
        To filter pending tasks for upcoming week: insert W
        To filter pending tasks for upcoming month: insert M
        To go back to main screen: insert Y
        """))


        match action:
            case "T":
                filterToday()
            case "W":
                filterWeek()
            case "M":
                filterMonth ()
            case "Y":
                main()
            case _:
                print("Invalid input. Please try again.")

def filterToday():
    for task in tasks:
        original_date = task[1]
        task_date = datetime.strptime(original_date, '%d.%m.%Y').date()

        if current_date == task_date:
            todayTasks.append(task)

    if todayTasks:
        print(f"Tasks for today are:")
        for (index, task) in enumerate(todayTasks):
                print(f"Task #{index+1}. {task}.")
    else:
        print(f"There are no tasks for today.")


def filterWeek():
    for task in tasks:
        original_date = task[1]
        task_date = datetime.strptime(original_date, '%d.%m.%Y').date()

        if current_date <= task_date <= week_from_now:
            weekTasks.append(task)

    if weekTasks:
        print(f"Tasks for the upcoming week are:")
        for (index, task) in enumerate(weekTasks):
                print(f"Task #{index+1}. {task}.")
    else:
        print(f"There are no tasks for the upcoming week.")


def filterMonth():
    for task in tasks:
        original_date = task[1]
        task_date = datetime.strptime(original_date, '%d.%m.%Y').date()

        if current_date <= task_date <= month_from_now:
            monthTasks.append(task)

    if monthTasks:
        print(f"Tasks for the upcoming month are:")
        for (index, task) in enumerate(monthTasks):
            print(f"Task #{index+1}. {task}.")
    else:
        print(f"There are no tasks for the upcoming month.")

def timeDuration():

    todayTasks.clear()
    weekTasks.clear()
    monthTasks.clear()

    print("\n-------------")
    category = [sublist[3] for sublist in tasks]
    unique_categories = list(set(category))
    print(f"Currently on your list there are tasks in the following categories:")
    for (index, element) in enumerate(unique_categories):
        print(f"#{index + 1}.{element}")
    print("-------------\n")

    applied_filter = input("What category do you want get duration summary for?\n")
    if applied_filter in category:
        filtered = list(filter(lambda x: x[3] == applied_filter, tasks))

        for task in filtered:
            original_date = task[1]
            task_date = datetime.strptime(original_date, '%d.%m.%Y').date()
            if current_date == task_date:
                todayTasks.append(task)
            if current_date <= task_date <= week_from_now:
                weekTasks.append(task)
            if current_date <= task_date <= month_from_now:
                monthTasks.append(task)

        duration_today = sum([sublist[2] for sublist in todayTasks])
        duration_week = sum([sublist[2] for sublist in weekTasks])
        duration_month = sum ([sublist[2] for sublist in monthTasks])

        if todayTasks:
            print(f"Today there are {duration_today} minutes planned for '{applied_filter}' category.")

        if weekTasks:
            print(f"This week there are {duration_week} minutes planned for '{applied_filter}' category.")

        if monthTasks:
            print(f"This month there are {duration_month} minutes planned for '{applied_filter}' category.")

    else:
        print(f"'{applied_filter}' category not found.")



def deleteTask():
    listTasks ()
    print("\n-------------")
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
        if taskToEdit >= 1 and taskToEdit < 1+len(tasks):
            tasks[taskToEdit-1]=[ input("Enter new value for task: "),
                                input("Enter new value for date [expected format: DD.MM.YYYY]: "),
                                int(input("Enter new value for duration time in minutes: ")),
                                input("Enter new value for category: "),
                                input("Enter new value for additional notes: ")]
            print(f"'{taskToEdit}' has been edited.")
        else:
            print(f"Task #{taskToEdit} has not been found.")
    except:
        print("Invalid input.")

def exportList():
    tasks_formatted = pd.DataFrame(tasks, columns=["task", "date", "duration (mins)", "category", "notes"])
    tasks_formatted.to_csv("tasks_formatted.csv", index=False)
    print("Tasks exported successfully. CSV file saved in the path for this library.")

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
        To filter tasks per category: insert FC
        To filter tasks per date: insert FD
        To get time summary per category: insert T
        To export the current list into CSV file: insert EL
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
            case "FC":
                filterCategory ()
            case "X":
                print("Ok, thank you for using this App, see you next time!\n-------------")
                not_stop_working = False
                print("\n-------------")
            case "FD":
                filterDate ()
            case "T":
                timeDuration()
            case "EL":
                exportList()
            case _:
                print("Invalid input. Please try again.")



if __name__ == "__main__":
    main()


