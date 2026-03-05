# Quick-Calc

## Project Description

Quick-Calc is a simple calculator application developed as part of the Software Testing & Quality Assurance practical assignment. The application performs basic arithmetic operations including addition, subtraction, multiplication, division, and a clear function.

The main purpose of this project is to demonstrate software testing practices such as unit testing and integration testing while maintaining proper version control using Git and GitHub.

---

## Features

* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division of two numbers
* Handles division by zero
* Clear function to reset the calculator

---

## Project Structure

```
swe-testing-assignment
│
├── calculator.py
├── app.py
├── README.md
├── TESTING.md
│
└── tests
    ├── test_calculator.py
    └── test_integration.py
```

* **calculator.py** – contains the core calculator logic
* **app.py** – simple command-line interface for user input
* **tests/** – contains unit and integration tests
* **README.md** – project documentation
* **TESTING.md** – testing strategy and explanations

---

## Setup Instructions

1. Clone the repository

```
git clone https://github.com/yourusername/swe-testing-assignment.git
```

2. Navigate into the project folder

```
cd swe-testing-assignment
```

3. Install required dependencies

```
pip install pytest
```

---

## Running the Application

To run the calculator application:

```
python app.py
```

The program will prompt the user to enter numbers and select an operation.

---

## Running the Tests

The project uses the **Pytest** testing framework.

To run the full test suite:

```
pytest
```

This command will automatically discover and execute all tests located in the `tests` directory.

---

## Testing Framework Research

### Pytest

Pytest is a widely used Python testing framework known for its simplicity and flexibility. It allows developers to write test cases using simple Python functions instead of complex class structures. Pytest provides features such as automatic test discovery, fixtures, and powerful assertion introspection, making it easier to write and maintain tests.

Another advantage of Pytest is that it requires less boilerplate code, which makes test files shorter and more readable. Because of these features, Pytest is commonly used in modern Python development projects.

### Unittest

Unittest is Python’s built-in testing framework and is inspired by the JUnit testing framework used in Java. It uses a class-based structure where test cases are organized into classes and methods. Unittest is reliable and stable since it is included in the Python standard library, meaning it does not require any external installation.

However, writing tests in Unittest often requires more code and setup compared to Pytest. Assertions are also less readable, which can make tests harder to understand for beginners.

### Framework Choice

For this project, **Pytest was chosen** as the primary testing framework. Pytest provides a simpler syntax, automatic test discovery, and better readability compared to Unittest. These features make it more suitable for small projects like Quick-Calc where quick development and clear test cases are important.

---

## Version

Current release: **v1.0.0**

This release includes the initial implementation of the Quick-Calc application along with unit tests, integration tests, and project documentation.

---

## Author

Paul Moses
Advanced Software Engineering – Practical Assignment
