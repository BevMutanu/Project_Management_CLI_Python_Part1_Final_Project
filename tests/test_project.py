from models.project import Project
from models.task import Task


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

