"""
helpers.py

Common helper functions.
"""


def find_user(users, name):
    """
    Find a user by name.
    """
    return next(
        (user for user in users if user["name"] == name),
        None
    )


def find_project(projects, title):
    """
    Find a project by title.
    """
    return next(
        (project for project in projects if project["title"] == title),
        None
    )


def find_task(tasks, title):
    """
    Find a task by title.
    """
    return next(
        (task for task in tasks if task["title"] == title),
        None
    )

