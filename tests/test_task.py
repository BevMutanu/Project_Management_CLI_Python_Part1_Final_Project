from models.task import Task
from models.project import Project
from models.user import User

import pytest


def test_empty_title_raises():
    with pytest.raises(ValueError):
        Task("", "Alice")


def test_empty_assigned_to_raises():
    with pytest.raises(ValueError):
        Task("Write docs", "")


def test_task_defaults():
    task = Task(
        "Write tests",
        "David",
    )

    assert task.status == "Pending"


def test_mark_complete():
    task = Task(
        "Deploy app",
        "Emma",
    )

    task.mark_complete()

    assert task.status == "Complete"

import pytest

def test_duplicate_tasks_raise():
    project = Project(
        "Website",
        "Build site",
        "2026-12-31",
    )

    project.add_task(Task("Deploy", "Alice"))

    with pytest.raises(ValueError):
        project.add_task(Task("Deploy", "Bob"))

import pytest

def test_duplicate_projects_raise():
    user = User(
        "Alice",
        "alice@example.com",
    )

    project = Project(
        "Website",
        "",
        "2026-12-31",
    )

    user.add_project(project)

    with pytest.raises(ValueError):
        user.add_project(
            Project(
                "Website",
                "",
                "2027-01-01",
            )
        )

