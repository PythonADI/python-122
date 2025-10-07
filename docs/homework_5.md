# Homework 5: Advanced Lists and Control Flow

## Instructions

Complete the following exercises using the code and concepts from `workshop_5`. All work should be committed to your GitHub repository.

### 1. List Modification
- Create a Python script that:
  - Creates a list of at least 10 numbers (mixed positive and negative)
  - Modifies specific elements by index (change at least 3 elements)
  - Prints the list before and after modification
  - Adds 5 to every element using a loop
  - Prints the final list
- Reference the approach shown in `modify_lists.py` and `lists.py`

### 2. List Slicing
- Write a script that:
  - Creates a list of at least 12 integers
  - Prints the first half of the list using slicing
  - Prints the second half of the list using slicing
  - Prints all elements with even indices using slicing
  - Prints all elements with odd indices using slicing
  - Prints every third element using slicing
  - Prints the list in reverse order using slicing
- Follow the pattern in `slices.py` but implement all the required slicing operations

### 3. List Filtering
- Create a script that:
  - Generates a list of 20 random integers between -100 and 100 (use `import random` and `random.randint(-100, 100)`)
  - Creates separate lists for:
    - Positive numbers
    - Negative numbers
    - Even numbers
    - Odd numbers
    - Numbers divisible by 5
  - Prints all the separate lists with appropriate labels
- Use techniques from `lists.py` and `pop.py`

### 4. Guard Clauses
- Write a script that validates a user's password with the following rules:
  - Must be at least 8 characters long
  - Must contain at least one uppercase letter
  - Must contain at least one lowercase letter
  - Must contain at least one digit
  - Must contain at least one special character (!@#$%^&*)
- Use guard clauses as shown in `guard_clause.py` to provide specific feedback about why the password is invalid
- Continue asking for a new password until all criteria are met

### 5. Interactive List Manager
- Create an interactive program that:
  - Presents a menu of options:
    1. Add a number to the list
    2. Remove a number from the list
    3. Display the current list
    4. Display the sum and average of the list
    5. Find the maximum and minimum values
    6. Clear the list
    7. Exit the program
  - Uses an infinite loop with appropriate break statements
  - Implements proper input validation for all operations
  - Provides user-friendly feedback for all actions
- Implement techniques from `infinite_loop.py` and other workshop files

### 6. List Partitioning Challenge
- Implement the challenge described in `challenge.py`:
  - Create a program that asks the user for numbers indefinitely
  - When the user types "done", stop taking new numbers and:
    1. Save each odd number in a separate list
    2. Save each number divisible by 7 in a separate list
    3. Save each number divisible by both 2 and 3 in a separate list
  - Print all three list contents with appropriate labels
  - Calculate and display the sum and average of each list

## Submission Guidelines
1. Create a folder named `homework_5` in your GitHub repository.
2. Create separate `.py` files for each exercise (6 files total).
3. Include meaningful comments in your code explaining your logic.
4. Make sure to commit and push your changes to GitHub.
5. Test all your scripts to ensure they work as expected.

## Evaluation Criteria
- Proper use of list operations and slicing
- Effective implementation of list filtering and partitioning
- Correct use of guard clauses
- Proper implementation of infinite loops with appropriate exit conditions
- Input validation and user feedback
- Code organization and readability
- Following the submission guidelines