from models.user import User
from models.project import Project


def test_create_user():
    user = User("Alice", "alice@example.com")

    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.projects == []


def test_add_project_to_user():
    user = User("Bob", "bob@example.com")
    project = Project(
        "Website",
        "Build company website",
        "2026-12-31",
    )

    user.add_project(project)

    assert len(user.projects) == 1
    assert user.projects[0].title == "Website"


def test_user_to_dict():
    user = User("Carol", "carol@example.com")

    data = user.to_dict()

    assert data["name"] == "Carol"
    assert data["email"] == "carol@example.com"

