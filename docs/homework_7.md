# Homework 7: Functions, Searching, and Sorting

## Instructions

Complete the following exercises using the code and concepts from `workshop_7`. All work should be committed to your GitHub repository.

### 1. Basic Functions
- Create a Python script that:
  - Defines at least 3 different functions with parameters
  - Each function should serve a specific purpose (e.g., mathematical calculations, string manipulation, list operations)
  - Demonstrates calling these functions with different arguments
  - Includes appropriate documentation for each function (comments explaining what the function does, parameters, and return values)
- Reference the approach shown in `basic_functions.py`

### 2. Function Return Values
- Write a script that:
  - Defines at least 3 functions that return different types of values (int, float, string, list, dictionary, etc.)
  - Shows how to capture and use the returned values in subsequent operations
  - Includes at least one function that returns multiple values (using tuples)
  - Demonstrates unpacking returned values into separate variables
- Follow the pattern in `return.py` but implement your own solution

### 3. Input Validation Function
- Create a script that:
  - Defines a function to validate user input for different data types (similar to `is_valid_number` in `function.py`)
  - Implements validation functions for at least 3 types of data:
    - Numeric input (integers or floats with proper format)
    - String input (e.g., checking for valid email format, or names with only alphabetic characters)
    - Date input (checking for proper date format)
  - Uses these validation functions in a simple program that collects and processes user input
- Reference the approach in `function.py`

### 4. Linear Search Implementation
- Write a script that:
  - Implements a linear search function that searches for a target value in a list
  - The function should take a list and target value as parameters and return the index if found or -1 if not found
  - Creates a list of at least 20 items (can be numbers, strings, or custom objects)
  - Demonstrates searching for at least 5 different values (some that exist in the list and some that don't)
  - Prints appropriate messages based on the search results
- Follow the pattern shown in the linear search part of `search.py`

### 5. Binary Search Implementation
- Create a program that:
  - Implements a binary search function for a sorted list
  - The function should take a sorted list and target value as parameters
  - Creates a sorted list of at least 20 numbers
  - Compares the efficiency of linear search vs. binary search by:
    - Counting the number of comparisons made in each approach
    - Reporting which search method was more efficient for different scenarios
  - Includes proper error handling (e.g., checking that the list is sorted before binary search)
- Reference the binary search implementation in `search.py`

### 6. Custom Sorting Algorithm (Challenge)
- Implement a simple sorting algorithm (like Selection Sort or Insertion Sort) from scratch:
  - Create a function that takes a list as a parameter and returns a sorted version
  - Add functionality to sort in either ascending or descending order
  - Include a parameter to sort by a specific key function (similar to the key parameter in Python's built-in sort)
  - Demonstrate your sorting algorithm with different types of data (numbers, strings, custom objects)
  - Compare your algorithm's efficiency with Python's built-in sorting functions
- Use concepts from `sorting.py` but implement your own solution

## Submission Guidelines
1. Create a folder named `homework_7` in your GitHub repository.
2. Create separate `.py` files for each exercise (6 files total).
3. Include meaningful comments in your code explaining your logic.
4. Make sure to commit and push your changes to GitHub.
5. Test all your scripts to ensure they work as expected.

## Evaluation Criteria
- Proper function definitions with appropriate parameters and return values
- Effective implementation of searching algorithms
- Correct implementation of sorting algorithms
- Understanding of algorithm efficiency
- Code organization and readability
- Proper documentation and comments
- Following the submission guidelines