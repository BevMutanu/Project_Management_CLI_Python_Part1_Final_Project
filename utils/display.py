"""
display.py

Utility functions for displaying users, projects, and tasks
using Rich tables.
"""

from rich.console import Console
from rich.table import Table

console = Console()


def show_users(users):
    """
    Display all users in a formatted table.

    Args:
        users (list[User]): List of User objects.
    """
    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return

    table = Table(title="Users")

    table.add_column("ID", justify="right")
    table.add_column("Name")
    table.add_column("Email")
    table.add_column("Projects", justify="center")

    for user in users:
        table.add_row(
            str(user.id),
            user.name,
            user.email,
            str(len(user.projects)),
        )

    console.print(table)


def show_projects(users):
    """
    Display all projects from all users.

    Args:
        users (list[User]): List of User objects.
    """
    table = Table(title="Projects")

    table.add_column("ID", justify="right")
    table.add_column("Title")
    table.add_column("Owner")
    table.add_column("Due Date")
    table.add_column("Tasks", justify="center")

    found = False

    for user in users:
        for project in user.projects:
            found = True
            table.add_row(
                str(project.id),
                project.title,
                user.name,
                project.due_date,
                str(len(project.tasks)),
            )

    if found:
        console.print(table)
    else:
        console.print("[yellow]No projects found.[/yellow]")


def show_tasks(users):
    """
    Display all tasks from every project.

    Args:
        users (list[User]): List of User objects.
    """
    table = Table(title="Tasks")

    table.add_column("ID", justify="right")
    table.add_column("Task")
    table.add_column("Project")
    table.add_column("Assigned To")
    table.add_column("Status")

    found = False

    for user in users:
        for project in user.projects:
            for task in project.tasks:
                found = True
                table.add_row(
                    str(task.id),
                    task.title,
                    project.title,
                    task.assigned_to,
                    task.status,
                )

    if found:
        console.print(table)
    else:
        console.print("[yellow]No tasks found.[/yellow]")

