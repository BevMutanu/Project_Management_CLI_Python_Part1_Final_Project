"""
task.py

Defines the Task class.
"""


class Task:
    """
    Represents a task belonging to a project.
    """

    id_counter = 1

    def __init__(self, title, assigned_to):
        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        if not assigned_to.strip():
            raise ValueError("Assigned user cannot be empty.")

        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    def mark_complete(self):
        """
        Mark the task as completed.
        """
        self.status = "Complete"

    def to_dict(self):
        """
        Convert the Task object into a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Task object from a dictionary.
        """
        task = cls(
            title=data["title"],
            assigned_to=data["assigned_to"],
        )

        task.id = data["id"]
        task.status = data.get("status", "Pending")

        if task.id >= cls.id_counter:
            cls.id_counter = task.id + 1

        return task

    def __str__(self):
        return (
            f"Task #{self.id}: {self.title} | "
            f"Assigned: {self.assigned_to} | "
            f"Status: {self.status}"
        )

