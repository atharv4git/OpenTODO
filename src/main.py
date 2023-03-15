import click
from Todolist import ToDoList
from termcolor import colored
import warnings
warnings.simplefilter('ignore')


@click.group()
def cli():
    pass


@cli.command()
def add_task():
    ToDoList().add_task()
    ToDoList().view_tasks()


@cli.command()
def del_task():
    ToDoList().del_task()
    ToDoList().view_tasks()


@cli.command()
def view_tasks():
    ToDoList().view_tasks()


@cli.command()
def mark_done():
    ToDoList().mark_done()
    ToDoList().view_tasks()


@cli.command()
def todo():
    ToDoList().view_not_done()


@cli.command()
def view_done():
    ToDoList().view_done()


if __name__ == '__main__':
    while True:
        opening = """

        ╭━━━╮╱╱╱╱╱╱╱╭━━━━┳━━━┳━━━┳━━━╮
        ┃╭━╮┃╱╱╱╱╱╱╱┃╭╮╭╮┃╭━╮┣╮╭╮┃╭━╮┃
        ┃┃╱┃┣━━┳━━┳━╋╯┃┃╰┫┃╱┃┃┃┃┃┃┃╱┃┃
        ┃┃╱┃┃╭╮┃┃━┫╭╮╮┃┃╱┃┃╱┃┃┃┃┃┃┃╱┃┃
        ┃╰━╯┃╰╯┃┃━┫┃┃┃┃┃╱┃╰━╯┣╯╰╯┃╰━╯┃
        ╰━━━┫╭━┻━━┻╯╰╯╰╯╱╰━━━┻━━━┻━━━╯
        ╱╱╱╱┃┃
        ╱╱╱╱╰╯"""
        print(opening)
        user_input = input(colored("Enter a command ('add_task', 'del_task', 'view_tasks', 'mark_done', 'todo' , 'view_done', or 'q' to quit): ", 'yellow', attrs=['bold']))
        if user_input == 'add_task':
            ToDoList().add_task()
        elif user_input == 'del_task':
            ToDoList().del_task()
        elif user_input == 'view_tasks':
            ToDoList().view_tasks()
        elif user_input == 'mark_done':
            ToDoList().mark_done()
        elif user_input == 'todo':
            ToDoList().view_not_done()
        elif user_input == 'view_done':
            ToDoList().view_done()
        elif user_input == 'q':
            break
        else:
            print("Invalid command. Please try again.")
