"""
storage.py

Handles loading and saving User objects.
"""

import json
import os

from models.user import User

DATABASE_PATH = "data/database.json"


def load_users():
    """
    Load User objects from the JSON database.
    """
    if not os.path.exists(DATABASE_PATH):
        return []

    try:
        with open(DATABASE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            User.from_dict(user_data)
            for user_data in data.get("users", [])
        ]

    except (json.JSONDecodeError, OSError):
        return []


def save_users(users):
    """
    Save User objects to the JSON database.
    """
    os.makedirs("data", exist_ok=True)

    data = {
        "users": [
            user.to_dict()
            for user in users
        ]
    }
    try:
        with open(DATABASE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError as exc:
        raise RuntimeError(f"Failed to save database: {exc}") from exc

