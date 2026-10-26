# LFIguard: A Python Path Validation

*Read this in other languages: [Русский](README_ru.md).*

## What is it?
**LFIguard** is a simple Python library to stop Path Traversal and Local File Inclusion attacks. It forces all file paths to stay inside one main folder. If a user tries to use shortcuts like `../` to break out, the library blocks them automatically, keeping your system safe.

## Table of Contents
- [What is it?](#what-is-it)
- [Main Features](#main-features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Code Examples](#code-examples)
- [Running Tests](#running-tests)
- [License](#license)

## Main Features
What LFIguard can do for you:
- **Defense:** Uses deep regex signatures to block tricky inputs (URL encoding, Unicode) and checks folder.
- **Crash Proof:** Safe handling of bad inputs (very long paths, bad characters, or symlink loops).
- **Strict Resolution:** Automatically clears all `.` and `..` shortcuts to find the real target file destination.
- **Zero Dependencies:** Pure Python solution with no external packages required.

## Dependencies
- **Python 3.10+**
- No external packages are required! LFIguard uses only standard built-in Python modules (`os`, `re`, `pathlib`, `unittest`).

## Installation

1. Clone the repository:
```bash
git clone https://github.com/splYozik/LFIguard.git
```

2. Go into the folder and install it locally using `pip`:
```bash
cd LFIguard
pip install .
```

## Code Examples
```python
from path_guard.protector import SafePathGuard

# 1. Initialize the guard with your main folder
guard = SafePathGuard("/var/www/app/uploads")

# 2. Example user input
user_input = "avatar.png"
if guard.is_safe_path(user_input):
    print("It's good! To open!")
else:
    print("Blocked!")

# 3. Dangerous paths will be blocked automatically
print(guard.is_safe_path("../../../etc/passwd"))           # False
print(guard.is_safe_path("%2e%2e%2f%2e%2e%2fetc/passwd"))  # False
print(guard.is_safe_path("secrets.yml"))                   # False
```

## Running Tests
To run the built-in tests, use this command in your terminal:
```bash
# go to the project root folder...
PYTHONPATH=. python3 tests/test_guard.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.