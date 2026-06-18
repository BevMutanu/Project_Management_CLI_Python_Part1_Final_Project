import pytest
from models.project import Project
from models.task import Task


def test_duplicate_tasks_raise():
    project = Project(
        "Website",
        "Build site",
        "2026-12-31",
    )

    project.add_task(Task("Deploy", "Alice"))

    with pytest.raises(ValueError):
        project.add_task(Task("Deploy", "Bob"))


def test_create_project():
    project = Project(
        "CLI Tool",
        "Python CLI application",
        "2026-08-01",
    )

    assert project.title == "CLI Tool"
    assert project.tasks == []


def test_add_task():
    project = Project(
        "Inventory",
        "Track stock",
        "2026-07-15",
    )

    task = Task(
        "Design database",
        "Alice",
    )

    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Design database"

