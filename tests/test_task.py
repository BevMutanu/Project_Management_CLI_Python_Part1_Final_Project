from models.task import Task


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

