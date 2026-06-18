"""
main.py

Command-line interface for the Project Management CLI.
"""

import argparse

from models.user import User
from models.project import Project
from models.task import Task

from utils.storage import load_users, save_users
from utils.display import show_users, show_projects, show_tasks


# Load persisted users when the application starts
users = load_users()


def add_user(args):
    """
    Add a new user to the system.
    """
    for user in users:
        if user.name.lower() == args.name.lower():
            print(f"User '{args.name}' already exists.")
            return

    new_user = User(args.name, args.email)
    users.append(new_user)
    save_users(users)

    print(f"User '{args.name}' added successfully.")


def add_project(args):
    """
    Add a project to an existing user.
    """
    owner = next(
        (
            user
            for user in users
            if user.name.lower() == args.user.lower()
        ),
        None,
    )

    if owner is None:
        print(f"User '{args.user}' not found.")
        return

    project = Project(
        title=args.title,
        description=args.description,
        due_date=args.due,
    )

    try:
        owner.add_project(project)
    except ValueError as exc:
        print(exc)
        return

    save_users(users)

    print(
        f"Project '{args.title}' added successfully to user '{owner.name}'."
    )


def add_task(args):
    """
    Add a task to an existing project.
    """
    for user in users:
        for project in user.projects:
            if project.title.lower() == args.project.lower():

                task = Task(
                    title=args.title,
                    assigned_to=args.assigned,
                )

                try:
                    project.add_task(task)
                except ValueError as exc:
                    print(exc)
                    return

                save_users(users)

                print(
                    f"Task '{args.title}' added to project "
                    f"'{project.title}'."
                )
                return

    print(f"Project '{args.project}' not found.")


def complete_task(args):
    """
    Mark a task as complete.
    """
    for user in users:
        for project in user.projects:
            for task in project.tasks:

                if task.title.lower() == args.title.lower():

                    if task.status == "Complete":
                        print("Task is already complete.")
                        return

                    task.mark_complete()
                    save_users(users)

                    print(
                        f"Task '{task.title}' marked as complete."
                    )
                    return

    print(f"Task '{args.title}' not found.")


def list_users(_args):
    """
    Display all users.
    """
    show_users(users)


def list_projects(_args):
    """
    Display all projects.
    """
    show_projects(users)


def list_tasks(_args):
    """
    Display all tasks.
    """
    show_tasks(users)


def build_parser():
    """
    Build and return the CLI argument parser.
    """
    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    subparsers = parser.add_subparsers(dest="command")


    # add-user

    add_user_parser = subparsers.add_parser(
        "add-user",
        help="Create a new user",
    )

    add_user_parser.add_argument(
        "--name",
        required=True,
        help="User's name",
    )

    add_user_parser.add_argument(
        "--email",
        required=True,
        help="User's email address",
    )

    add_user_parser.set_defaults(func=add_user)


    # add-project

    add_project_parser = subparsers.add_parser(
        "add-project",
        help="Create a project for a user",
    )

    add_project_parser.add_argument(
        "--user",
        required=True,
        help="Owner of the project",
    )

    add_project_parser.add_argument(
        "--title",
        required=True,
        help="Project title",
    )

    add_project_parser.add_argument(
        "--description",
        default="",
        help="Project description",
    )

    add_project_parser.add_argument(
        "--due",
        required=True,
        help="Due date",
    )

    add_project_parser.set_defaults(func=add_project)


    # add-task

    add_task_parser = subparsers.add_parser(
        "add-task",
        help="Add a task to a project",
    )

    add_task_parser.add_argument(
        "--project",
        required=True,
        help="Project title",
    )

    add_task_parser.add_argument(
        "--title",
        required=True,
        help="Task title",
    )

    add_task_parser.add_argument(
        "--assigned",
        required=True,
        help="Person assigned to the task",
    )

    add_task_parser.set_defaults(func=add_task)


    # complete-task

    complete_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as complete",
    )

    complete_parser.add_argument(
        "--title",
        required=True,
        help="Task title",
    )

    complete_parser.set_defaults(func=complete_task)


    # list-users

    list_users_parser = subparsers.add_parser(
        "list-users",
        help="Display all users",
    )

    list_users_parser.set_defaults(func=list_users)


    # list-projects

    list_projects_parser = subparsers.add_parser(
        "list-projects",
        help="Display all projects",
    )

    list_projects_parser.set_defaults(func=list_projects)


    # list-tasks

    list_tasks_parser = subparsers.add_parser(
        "list-tasks",
        help="Display all tasks",
    )

    list_tasks_parser.set_defaults(func=list_tasks)

    return parser


def main():
    """
    Application entry point.
    """
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

