"""
helpers.py

Common helper functions.
"""


def find_user(users, name):
    return next(
        (
            user
            for user in users
            if user.name.lower() == name.lower()
        ),
        None,
    )


def find_project(projects, title):
    return next(
        (
            project
            for project in projects
            if project.title.lower() == title.lower()
        ),
        None,
    )


def find_task(tasks, title):
    return next(
        (
            task
            for task in tasks
            if task.title.lower() == title.lower()
        ),
        None,
    )

