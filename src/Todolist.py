import datetime
import os
import warnings

import pandas as pd

from Task import Task

warnings.simplefilter('ignore')


class ToDoList:
    def __init__(self):
        if os.path.exists("./tasks.csv"):
            self.tasks = pd.read_csv("tasks.csv")
        else:
            tasks = pd.DataFrame(columns=["id", "name", "desc", "completed", "datetime"])
            tasks.to_csv("tasks.csv")
            self.tasks = pd.read_csv("tasks.csv")

    def add_task(self):
        name = input("Enter name of the Task: ")
        desc = input("Enter the description of the Task: ")
        id = len(self.tasks)
        newTask = Task(id + 1, name, desc, False, datetime.datetime.now())
        task_series = pd.Series(
            {'id': newTask.id, 'name': newTask.name, 'desc': newTask.desc, 'completed': newTask.completed,
             'datetime': newTask.datetime})
        print(task_series)
        self.tasks = self.tasks.append(task_series, ignore_index=True)
        self.tasks.to_csv("tasks.csv", index=True, columns=["id", "name", "desc", "completed", "datetime"])

    def del_task(self):
        id = int(input("Enter the ID of the task to be deleted: "))
        updatedDF = self.tasks.drop(index=id - 1, axis=0)
        updatedDF.to_csv("tasks.csv", index=True, columns=["id", "name", "desc", "completed", "datetime"])

    def view_tasks(self):
        print(self.tasks)

    def mark_done(self):
        print(self.tasks)
        id = int(input("Enter the ID of the task to be marked DONE✅: "))
        self.tasks.loc[id - 1, 'completed'] = True
        self.tasks.to_csv("tasks.csv", index=True, columns=["id", "name", "desc", "completed", "datetime"])
        print(self.tasks)

    def view_done(self):
        print(self.tasks[self.tasks.completed == True])

    def view_not_done(self):
        print(self.tasks[self.tasks.completed == False])
