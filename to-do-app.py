task=[]
tasks=[]
filtered=[]

todayTasks = []
weekTasks = []
monthTasks = []

import datetime
from datetime import datetime, timedelta

import random

import pandas as pd

current_date = datetime.now().date()
week_from_now = current_date + timedelta(weeks=1)
month_from_now = current_date + timedelta(days=30)

def loadTasks():
    try:
        tasks_data = pd.read_csv(f"to_do_list_{current_date}.csv")
        for index, row in tasks_data.iterrows():
            task = [
                row["task"],
                row["date"],
                int(row["duration (mins)"]),
                row["category"],
                row["notes"]
            ]
            tasks.append(task)
        print("Previous tasks loaded successfully!\n")

    except FileNotFoundError:
        print("No previous tasks file found. Starting with an empty list.\n")

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

def createDummyList():
    tasks_name = ["SOP update", "1:1 meeting", "team meeting", "revenue analysis", "cost adjustments",
                  "mandatory trainings", "improvement project", "manual payment"]

    tasks_duration = {
        "SOP update": [60, 240],
        "1:1 meeting": [30, 60],
        "team meeting": [30, 45],
        "revenue analysis": [170, 320],
        "cost adjustments": [15, 45],
        "mandatory trainings": [20, 65],
        "improvement project": [90, 160],
        "manual payment": [15, 75]}

    categories = ["high priority", "medium priority", "low priority"]

    notes = ["boring", "fun one", "exciting", "repetitive"]

    def random_date(start, end):
        delta = end - start
        random_days = random.randint(0, delta.days)
        return (start + timedelta(days=random_days)).strftime("%d.%m.%Y")

    start_date = datetime(2024, 10, 1)
    end_date = datetime(2024, 12, 31)

    def create_dummy_task():
        dummy_name = random.choice(tasks_name)
        dummy_date = random_date(start_date, end_date)
        dummy_duration = int(random.randint(*tasks_duration[dummy_name]))
        dummy_category = random.choice(categories)
        dummy_note = random.choice(notes)
        return dummy_name, dummy_date, dummy_duration, dummy_category, dummy_note

    def create_dummy_tasks(tasks_number):
        dummy_tasks_list = []
        for _ in range(tasks_number):
            dummy_tasks_list.append(create_dummy_task())
        return dummy_tasks_list

    def exportDummyTasks():
        dummy_tasks_formatted = pd.DataFrame(dummy_tasks, columns=["task", "date", "duration (mins)", "category", "notes"])
        dummy_tasks_formatted.to_csv(f"dummy_to_do_list_{current_date}.csv", index=False, header=True)
        print(f"Tasks exported successfully. CSV file 'dummy_to_do_list_{current_date}' saved in the project path.")

    tasks_number = int(input("Enter the # of tasks: "))
    dummy_tasks = create_dummy_tasks(tasks_number)
    exportDummyTasks()



def exportList():
    tasks_formatted = pd.DataFrame(tasks, columns=["task", "date", "duration (mins)", "category", "notes"])
    tasks_formatted.to_csv(f"to_do_list_{current_date}.csv", index=False)
    print(f"Tasks exported successfully. CSV file 'to_do_list_{current_date}' saved in the project path.")

def main ():
    print("-------------\nHello in Your-To-Do-List App!\n-------------")

    load_previous = input("Would you like to load your previous task list? (Yes/No):\n")
    if load_previous == "Yes":
        loadTasks()

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
        To create the dummy list: insert DL
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
            case "FD":
                filterDate ()
            case "T":
                timeDuration()
            case "EL":
                exportList()
            case "DL":
                createDummyList()
            case "X":
                print("Ok, thank you for using this App, see you next time!\n-------------")
                not_stop_working = False
                print("\n-------------")
            case _:
                print("Invalid input. Please try again.")




if __name__ == "__main__":
    main()


