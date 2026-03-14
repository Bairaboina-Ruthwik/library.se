# Library Book Management System

## Course
CS2042 – Software Engineering

## Assignment
Agile Development with Git and Unit Testing (Assignment #1)

## Description
This project implements a **Library Book Management System** using Python.
The system is developed by following a **three-sprint Agile process** with
proper **Git discipline** and **unit testing**.

The system uses **in-memory data structures only** (no database) and supports:
- Book registration
- Borrowing and returning books
- Generating a library status report

---

## Technology Stack
- Programming Language: Python
- Testing Framework: unittest
- Version Control: Git
- Database: Not used (in-memory only)

## Project Structure

```
library-se/
│
├── src/
│   └── library.py
│
├── tests/
│   └── test_library.py
│
├── docs/
│   ├── USER_STORIES.md
│   └── TRACEABILITY.md
│
├── README.md
└── .gitignore
```

## Sprint-wise Implementation

### Sprint 1: Book Registration
- Add books with Book ID, title, and author
- Prevent duplicate Book IDs
- Git branch: `feature/sprint-1`
- Git tag: `v0.1`

### Sprint 2: Borrow and Return Book
- Borrow available books
- Return borrowed books
- Prevent borrowing an already borrowed book
- Git branch: `feature/sprint-2`
- Git tag: `v0.2`

### Sprint 3: Library Report
- Generate library report with book status
- Git branch: `feature/sprint-3`
- Git tag: `v0.3`

---

## Running Unit Tests

Run all tests using the following command:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
