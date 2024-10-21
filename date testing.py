tasks=[['jump', '29.10.2024', '15', 'sport', 'high'],
        ['paint something', '01.11.2024', '90', 'art', 'none'],
        ['run', '30.10.2024', '60', 'sport', 'fast'],
        ['go to the cinema', '06.11.2024', '150', 'entertainment', 'popcorn'],
        ['buy coat', '20.11.2024', '15', 'shopping', 'none']]

todayTasks = []
weekTasks = []
monthTasks = []

import datetime
current_date = datetime.date(2024, 10, 29)
tdelta_week = datetime.timedelta(days=7)
week_date = current_date + tdelta_week
tdelta_month = datetime.timedelta(days=30)
month_date = current_date + tdelta_month

from datetime import datetime

for task in tasks:
    original_date = task[1]
    task_date = datetime.strptime(original_date, '%d.%m.%Y')
    task[1] = task_date.strftime('%Y-%m-%d')

task_dates = [sublist[1] for sublist in tasks]

#printing to check if it works:
print(current_date)
print(task_dates)
print(tasks)
#it works!
#output:
#2024-10-29
#['2024-10-29', '2024-11-01', '2024-10-30', '2024-11-06', '2024-11-20']
#[['jump', '2024-10-29', '15', 'sport', 'high'], ['paint something', '2024-11-01', '90', 'art', 'none'], ['run', '2024-10-30', '60', 'sport', 'fast'], ['go to the cinema', '2024-11-06', '150', 'entertainment', 'popcorn'], ['buy coat', '2024-11-20', '15', 'shopping', 'none']]

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
    if current_date in task_dates:
        todayTasks = list(filter(lambda x: x[1] == current_date, tasks))
        print(f"Tasks for today are:")
        for (index, task) in enumerate(todayTasks):
            print(f"Task #{index}. {task}.")
    else:
        print(f"There are no tasks for today.")

def filterWeek():
    if week_date in task_dates:
        weekTasks = list(filter(lambda x: x[1] <= week_date, tasks))
        print(f"Tasks for upcoming week are:")
        for (index, task) in enumerate(weekTasks):
            print(f"Task #{index}. {task}.")
    else:
        print(f"There are no tasks for upcoming week.")

def filterMonth():
    if month_date in task_dates:
        monthTasks = list(filter(lambda x: x[1] <= month_date, tasks))
        print(f"Tasks for upcoming month are:")
        for (index, task) in enumerate(monthTasks):
            print(f"Task #{index}. {task}.")
    else:
        print(f"There are no tasks for upcoming month.")

filterDate()

