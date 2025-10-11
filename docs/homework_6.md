# Homework 6: Dictionaries, Tuples, and Advanced Data Structures

## Instructions

Complete the following exercises using the code and concepts from `workshop_6`. All work should be committed to your GitHub repository.

### 1. Dictionary Operations
- Create a Python script that:
  - Creates a dictionary representing a student with keys for name, age, courses (a list), and GPA
  - Prints the entire dictionary
  - Accesses and prints specific values using keys
  - Modifies at least two values in the dictionary
  - Adds at least two new key-value pairs
  - Removes at least one key-value pair
  - Prints the final dictionary
- Reference the approach shown in `dicts.py`

### 2. Dictionary Iteration
- Write a script that:
  - Creates a dictionary of at least 5 countries as keys and their capitals as values
  - Uses different dictionary methods (keys(), values(), items()) to iterate through the dictionary
  - Formats and prints the data in a readable way (e.g., "The capital of [country] is [capital]")
  - Creates a new dictionary where the keys and values are swapped (capitals become keys, countries become values)
  - Prints the new dictionary
- Follow the pattern in `dicts.py` but implement your own solution

### 3. Tuple Implementation
- Create a script that:
  - Creates at least 3 different tuples representing various data (e.g., geographic coordinates, RGB colors, date components)
  - Demonstrates accessing tuple elements by index
  - Demonstrates unpacking tuples into separate variables
  - Uses tuples as dictionary keys (research how to do this)
  - Shows an example of when tuples are preferable to lists
- Reference the approach in `tuples.py`

### 4. Nested Data Structures
- Write a script that:
  - Creates a list of dictionaries where each dictionary represents a different product with keys for name, price, category, and stock
  - Implements a search function that allows the user to search products by name or category
  - Implements a filter function that shows products below a certain price or with stock above a certain threshold
  - Calculates and displays the total value of all products (price × stock)
- Follow the pattern shown in `nested_dict.py`

### 5. Student Grade Tracker
- Create a program that:
  - Allows the user to enter student names and scores for multiple subjects
  - Stores this data in an appropriate nested data structure (dictionaries inside a dictionary or list)
  - Calculates and displays each student's average score
  - Identifies and displays the highest scoring student for each subject
  - Calculates and displays the class average for each subject
- Reference the concepts from `nested_dict.py` and `arctic.py`

### 6. Temperature Analysis (Challenge)
- Extend the temperature analysis from `arctic.py` with the following enhancements:
  - Store temperature data as tuples with (day, temperature) pairs
  - Convert the data to a dictionary with days as keys and temperatures as values
  - Allow the user to:
    - Add new temperature readings
    - Find the average temperature for a specific range of days
    - Identify days with temperatures above or below a certain threshold
    - Display all recorded temperatures in ascending or descending order
  - Use appropriate dictionary and tuple operations for all functionality

## Submission Guidelines
1. Create a folder named `homework_6` in your GitHub repository.
2. Create separate `.py` files for each exercise (6 files total).
3. Include meaningful comments in your code explaining your logic.
4. Make sure to commit and push your changes to GitHub.
5. Test all your scripts to ensure they work as expected.

## Evaluation Criteria
- Proper use of dictionaries and dictionary methods
- Effective implementation of tuples and their operations
- Correct use of nested data structures
- Appropriate data structure selection for each task
- Input validation and user feedback
- Code organization and readability
- Following the submission guidelines