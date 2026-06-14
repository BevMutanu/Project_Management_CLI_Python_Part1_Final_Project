import json

from models.user import User
from utils.storage import save_users, load_users


def test_save_and_load_users():
    user = User(
        "Test User",
        "test@example.com",
    )

    save_users([user])

    loaded = load_users()

    assert len(loaded) >= 1
    assert loaded[0].name == "Test User"


def test_database_file_is_valid_json():
    with open(
        "data/database.json",
        "r",
        encoding="utf-8",
    ) as file:

        data = json.load(file)

    assert isinstance(data, dict)
    assert "users" in data

