# Project Management CLI

## Overview

Project Management CLI is a Python command-line application that allows administrators to manage users, projects, and tasks. It demonstrates object-oriented programming principles, JSON file persistence, modular design, and command-line interaction using `argparse`.

The application stores all data locally in a JSON file while maintaining the relationships between users, projects, and tasks.

---

## Features

* Create users
* Create projects and assign them to users
* Create tasks and assign them to projects
* Mark tasks as complete
* List all users
* List all projects
* List all tasks
* Persist data automatically using JSON
* Object-oriented architecture with inheritance and encapsulation
* Rich-formatted tables for improved command-line output

---

## Project Structure

```
project-management-cli/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── database.json
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── utils/
│   ├── __init__.py
│   ├── storage.py
│   ├── helpers.py
│   └── display.py
│
└── tests/
    ├── test_user.py
    ├── test_project.py
    ├── test_task.py
    └── test_storage.py
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd project-management-cli
```

Create and activate a virtual environment:

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Add a user

```bash
python main.py add-user \
    --name "Alex" \
    --email "alex@example.com"
```

### Add a project

```bash
python main.py add-project \
    --user "Alex" \
    --title "CLI Tool" \
    --description "Final project" \
    --due "2026-08-01"
```

### Add a task

```bash
python main.py add-task \
    --project "CLI Tool" \
    --title "Implement parser" \
    --assigned "Alex"
```

### Complete a task

```bash
python main.py complete-task \
    --title "Implement parser"
```

### List users

```bash
python main.py list-users
```

### List projects

```bash
python main.py list-projects
```

### List tasks

```bash
python main.py list-tasks
```

---

## Running Tests

Run all tests with:

```bash
pytest
```

Or run an individual test file:

```bash
pytest tests/test_user.py
```

---

## Technologies Used

* Python 3
* argparse
* JSON
* rich
* pytest

---

## Object-Oriented Design

The application uses the following relationships:

* `Person` → `User` (inheritance)
* `User` → multiple `Project` objects
* `Project` → multiple `Task` objects

Each model supports serialization through `to_dict()` and reconstruction through `from_dict()`.

---

## Data Persistence

Application data is stored in:

```
data/database.json
```

The JSON file is automatically loaded when the application starts and updated whenever changes are made.

---

## Future Improvements

* Delete users, projects, and tasks
* Edit existing records
* Search functionality
* Due date validation
* Task priorities
* Multiple contributors per project
* Colored status indicators
* Export reports to CSV or PDF

---

## License

This project is provided for educational purposes.
