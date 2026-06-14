"""
user.py

Defines the User class.
"""

from models.person import Person
from models.project import Project


class User(Person):
    """
    Represents a project management user.
    """

    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name, email)

        self.id = User.id_counter
        User.id_counter += 1

        self.projects = []

    def add_project(self, project):
        """
        Associate a Project object with this user.
        """
        self.projects.append(project)

    def to_dict(self):
        """
        Convert the User object into a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [
                project.to_dict()
                for project in self.projects
            ],
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a User object from a dictionary.
        """
        user = cls(
            name=data["name"],
            email=data["email"],
        )

        user.id = data["id"]

        if user.id >= cls.id_counter:
            cls.id_counter = user.id + 1

        user.projects = [
            Project.from_dict(project)
            for project in data.get("projects", [])
        ]

        return user

    def __str__(self):
        return (
            f"User #{self.id}: "
            f"{self.name} "
            f"({self.email}) - "
            f"{len(self.projects)} project(s)"
        )

