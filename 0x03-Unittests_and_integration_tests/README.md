# 0x03. Unittests and Integration Tests

## Overview:
This project focuses on writing unit and integration tests in Python using the `unittest` framework and mock objects to simulate external dependencies. You will learn to test functions, mock external calls, and ensure different parts of the system work together.

## Files:
- **`utils.py`**: Contains utility functions like `access_nested_map`, `get_json`, and the `memoize` decorator.
- **`client.py`**: Implements the `GithubOrgClient` class for interacting with GitHub's API.
- **`fixtures.py`**: Provides example data (fixtures) for testing API responses.
- **`test_utils.py`**: Unit tests for the functions in `utils.py`, using parameterized tests and mocks.
- **`test_client.py`**: Unit and integration tests for `GithubOrgClient`, mocking API calls and testing interactions.


