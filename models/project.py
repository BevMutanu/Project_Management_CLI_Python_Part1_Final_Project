"""
project.py

Defines the Project class.
"""

from models.task import Task


class Project:
    """
    Represents a project owned by a user.
    """

    id_counter = 1

    def __init__(self, title, description, due_date):
        self.id = Project.id_counter
        Project.id_counter += 1
        if not title.strip():
            raise ValueError("Project title cannot be empty.")

        if not due_date.strip():
            raise ValueError("Due date cannot be empty.")

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        for existing in self.tasks:
            if existing.title.lower() == task.title.lower():
                raise ValueError(
                    f"Task '{task.title}' already exists."
                )

        self.tasks.append(task)

    def to_dict(self):
        """
        Convert the Project object into a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [
                task.to_dict()
                for task in self.tasks
            ],
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Project object from a dictionary.
        """
        project = cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
        )

        project.id = data["id"]

        if project.id >= cls.id_counter:
            cls.id_counter = project.id + 1

        project.tasks = [
            Task.from_dict(task)
            for task in data.get("tasks", [])
        ]

        return project

    def __str__(self):
        return (
            f"Project #{self.id}: "
            f"{self.title} "
            f"({len(self.tasks)} task(s))"
        )

