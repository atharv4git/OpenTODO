# OpenTODO

```
╭━━━╮╱╱╱╱╱╱╱╭━━━━┳━━━┳━━━┳━━━╮
┃╭━╮┃╱╱╱╱╱╱╱┃╭╮╭╮┃╭━╮┣╮╭╮┃╭━╮┃
┃┃╱┃┣━━┳━━┳━╋╯┃┃╰┫┃╱┃┃┃┃┃┃┃╱┃┃
┃┃╱┃┃╭╮┃┃━┫╭╮╮┃┃╱┃┃╱┃┃┃┃┃┃┃╱┃┃
┃╰━╯┃╰╯┃┃━┫┃┃┃┃┃╱┃╰━╯┣╯╰╯┃╰━╯┃
╰━━━┫╭━┻━━┻╯╰╯╰╯╱╰━━━┻━━━┻━━━╯
╱╱╱╱┃┃
╱╱╱╱╰╯
```

## How to use:
```commandline
git clone https://github.com/atharv4git/OpenTODO.git
```
```commandline
pip install requirments.txt
```
```commandline
python src/main.py
```


## Project Description:
In this project, you will create a simple to-do list manager that allows users to add, delete, and view their to-do items. The to-do list manager will be a command-line application that the user can interact with by typing in commands.

Here are the basic features that your to-do list manager should have:

1. Add a new task to the to-do list.
2. Delete a task from the to-do list.
3. View the entire to-do list.
4. Save the to-do list to a file.
5. Load the to-do list from a file.

Here's an example of how the user interface might look like:
```commandline
Welcome to the To-Do List Manager!

Commands:
    add: add a new task to the to-do list
    delete: delete a task from the to-do list
    view: view the entire to-do list
    save: save the to-do list to a file
    load: load the to-do list from a file
    quit: exit the to-do list manager

Enter command: add
Enter task description: Buy milk

Enter command: add
Enter task description: Go to the gym

Enter command: view
To-Do List:
1. Buy milk
2. Go to the gym

Enter command: delete
Enter task number to delete: 1

Enter command: view
To-Do List:
1. Go to the gym

Enter command: save
Enter file name: todo.txt

Enter command: quit

```
You can add more features to this project as you wish, such as sorting tasks by priority or due date, adding categories, etc. Good luck!