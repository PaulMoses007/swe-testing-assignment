# Testing Strategy

## Overview

The Quick-Calc project uses a structured testing approach to verify the correctness and reliability of the calculator application. The testing process focuses primarily on validating the arithmetic operations implemented in the calculator logic and ensuring that different parts of the application interact correctly.

The testing strategy combines **unit testing** and **integration testing** to provide confidence that the system behaves as expected.

---

## What Was Tested

The following functionality of the Quick-Calc application was tested:

* Addition operation
* Subtraction operation
* Multiplication operation
* Division operation
* Division-by-zero handling
* Negative number calculations
* Decimal number calculations
* Large number calculations
* Clear function behavior
* Interaction between calculation logic and application flow

These tests ensure that the core logic of the calculator works correctly under different conditions.

---

## What Was Not Tested

Some aspects of the system were intentionally not tested because they are outside the scope of this small project:

* Performance testing
* Security testing
* Graphical user interface behavior
* Stress testing
* Cross-platform compatibility

The main focus of this project is validating the correctness of the calculation logic and demonstrating proper testing practices.

---

## Testing Pyramid

The testing approach follows the **Testing Pyramid** principle.

The testing pyramid suggests having:

* Many **unit tests**
* Fewer **integration tests**
* Very few **end-to-end tests**

In this project:

* **Unit tests** verify individual functions in the calculator logic.
* **Integration tests** verify that different parts of the application work together.

Most of the tests in this project are unit tests because they are fast, simple, and isolate specific functionality.

---

## Black-Box vs White-Box Testing

### White-Box Testing

Unit tests in this project follow **white-box testing** principles because they directly test the internal functions of the `Calculator` class. The internal logic of the application is known and used when writing the tests.

### Black-Box Testing

Integration tests represent **black-box testing** because they test the behavior of the application from the user’s perspective without focusing on internal implementation details.

---

## Functional vs Non-Functional Testing

This project focuses on **functional testing**, which verifies that the calculator performs arithmetic operations correctly.

Examples of functional tests include:

* Verifying that 5 + 3 returns 8
* Verifying multiplication results
* Checking that division by zero raises an error

Non-functional testing such as performance, scalability, and usability testing was not included because the Quick-Calc application is a simple demonstration project.

---

## Regression Testing

Regression testing ensures that existing functionality continues to work when new features or changes are introduced.

The test suite in this project can be used for regression testing by running the tests after any code modification. If any test fails, it indicates that a previously working feature may have been broken.

Running the test suite regularly helps detect bugs early and maintain code stability.

---

## Test Results Summary

| Test Name             | Type             | Result |
| --------------------- | ---------------- | ------ |
| test_add              | Unit Test        | Pass   |
| test_subtract         | Unit Test        | Pass   |
| test_multiply         | Unit Test        | Pass   |
| test_divide           | Unit Test        | Pass   |
| test_divide_by_zero   | Unit Test        | Pass   |
| test_negative_numbers | Unit Test        | Pass   |
| test_decimal_numbers  | Unit Test        | Pass   |
| test_large_numbers    | Unit Test        | Pass   |
| test_full_calculation | Integration Test | Pass   |
| test_clear_function   | Integration Test | Pass   |

All tests passed successfully and confirmed that the calculator logic behaves as expected.

---

## Conclusion

The implemented testing strategy ensures that the Quick-Calc application functions correctly and demonstrates the importance of automated testing in software development. By combining unit tests and integration tests, the project verifies both individual components and the interaction between them.
