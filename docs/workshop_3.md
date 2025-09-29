# Workshop 3: Control Flow and Loops in Python

## Prerequisites:
- Completion of Workshop 1 and Workshop 2
- Basic understanding of Python syntax, variables, and data types
- Python installed on your computer
- IDE or text editor

## What will you learn in this workshop?
- [Control Flow](#control-flow)
  - [Conditional Statements (if, elif, else)](#conditional-statements)
  - [Comparison and Logical Operators](#comparison-and-logical-operators)
  - [Nested Conditions](#nested-conditions)
- [Loops](#loops)
  - [For Loops and range()](#for-loops)
  - [While Loops](#while-loops)
  - [Loop Control (break, continue)](#loop-control)
  - [Nested Loops](#nested-loops)
- [Practice Problems](#practice-problems)

## Control Flow

### Conditional Statements
Conditional statements allow your program to make decisions based on conditions.

#### Basic if-elif-else
```python
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
```

#### Multiple conditions example
```python
grade = 85

if grade >= 90:
    print("A - Excellent!")
elif grade >= 80:
    print("B - Good job!")
elif grade >= 70:
    print("C - Not bad.")
elif grade >= 60:
    print("D - You need to study more.")
else:
    print("F - You failed.")
```

#### Ternary operator (one-line if statement)
```python
temperature = 35
status = "Hot" if temperature > 30 else "Not hot"
print(status)  # Prints: Hot
```

### Comparison and Logical Operators
Comparison operators are used to compare values:
- `==` - Equal to
- `!=` - Not equal to
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal to
- `>=` - Greater than or equal to

Logical operators combine conditions:
- `and` - Both conditions must be true
- `or` - At least one condition must be true
- `not` - Inverts the condition

#### Comparison operators example
```python
x = 10
y = 20

# Using comparison operators
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
```

#### Logical operators example
```python
x = 10
y = 20

# Using logical operators
if x > 5 and y < 30:
    print("Both conditions are true")

if x > 15 or y > 15:
    print("At least one condition is true")

if not x > y:
    print("x is not greater than y")
```

### Nested Conditions
You can nest conditional statements inside each other:

#### Nested if-else example
```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive a car.")
    else:
        print("You are old enough, but you need a license.")
else:
    print("You are too young to drive.")
```

#### Complex nested condition example
```python
score = 85
attendance = 95
bonus_points = 5

if score >= 70:
    if attendance >= 80:
        final_grade = score + bonus_points
        if final_grade >= 90:
            print("Your grade is A")
        else:
            print("Your grade is B")
    else:
        print("Good score, but attendance too low")
else:
    print("You need to improve your score")
```

## Loops

### For Loops and range()
For loops iterate over a sequence (like a range, string, or other iterable). The `range()` function is particularly useful with for loops to generate sequences of numbers.

#### Basic range() function
```python
# range(stop) - Generates numbers from 0 up to (but not including) stop
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4
```

#### Range with start and stop values
```python
# range(start, stop) - Generates numbers from start up to (but not including) stop
for i in range(2, 8):
    print(i)  # Prints 2, 3, 4, 5, 6, 7
```

#### Range with start, stop, and step values
```python
# range(start, stop, step) - Generates numbers with given step
for i in range(1, 10, 2):
    print(i)  # Prints 1, 3, 5, 7, 9
```

#### Range with negative step (counting backwards)
```python
for i in range(10, 0, -1):
    print(i)  # Prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

#### Iterating through a string
```python
for char in "Python":
    print(char)  # Prints P, y, t, h, o, n on separate lines
```

#### Using enumerate for index and value
```python
for index, char in enumerate("Hello"):
    print(f"Character at position {index}: {char}")
```

#### For loop with else clause
```python
# The else clause executes after the loop completes normally (not via break)
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")
```

#### Using range with conditional statements
```python
# Finding even numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")  # Prints 2, 4, 6, 8, 10 with labels
```

#### Other useful range() operations
```python
# Sum of numbers using range
total = sum(range(1, 101))
print(f"Sum of numbers 1-100: {total}")  # Prints: 5050x

# Using range for specific patterns
print("Multiples of 3 from 0 to 30:")
for i in range(0, 31, 3):
    print(i, end=" ")  # Prints: 0 3 6 9 12 15 18 21 24 27 30
```

### While Loops
While loops continue as long as a condition is true:

#### Basic while loop
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count by 1
```

#### Using while with a sentinel value
```python
# Note: this would normally require user input
answer = ""
while answer != "quit":
    print("Current answer:", answer)
    answer = "quit"  # Normally this would be input("Enter 'quit' to exit: ")
```

#### Infinite loop with break
```python
# This pattern is common when requiring continuous user interaction
while True:
    # user_input = input("Type 'exit' to quit: ")
    user_input = "exit"  # Simulating input for documentation
    print("You entered:", user_input)
    if user_input.lower() == 'exit':
        break
```

#### While loop with else clause
```python
counter = 0
while counter < 3:
    print(counter)
    counter += 1
else:
    print("While loop completed!")
```

### Loop Control
Control statements for loops:
- `break` - Exits the loop completely
- `continue` - Skips the current iteration and continues with the next

#### Using break
```python
# Using break to exit a loop early
print("Break example:")
for i in range(10):
    if i == 5:
        print("Found 5! Breaking the loop.")
        break
    print(i)  # Prints 0, 1, 2, 3, 4
```

#### Using continue
```python
print("Continue example:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints 1, 3, 5, 7, 9
```

#### Nested loops with break
```python
print("Nested loops with break:")
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 1:
            print(f"  Found j=1, breaking inner loop")
            break
        print(f"  Inner loop: {j}")
```

#### While loop with break
```python
print("While loop with break:")
counter = 0
while True:  # Infinite loop
    counter += 1
    if counter > 5:
        print("Counter exceeded 5, breaking out")
        break
    print(f"Counter: {counter}")
```

## Practice Problems

1. **Temperature Converter**
   - Write a program that converts temperature from Celsius to Fahrenheit
   - Formula: F = C * 9/5 + 32
   - Ask the user to enter a temperature in Celsius
   - Use an if statement to tell the user if it's hot (>30°C), moderate (15-30°C), or cold (<15°C)
   - Example output:
     ```
     Enter temperature in Celsius: 35
     35°C is 95.0°F
     It's hot!
     ```

2. **Number Guessing Game**
   - Create a simple game where the computer generates a random number (between 1-100)
   - The user tries to guess it
   - Use loops to allow multiple guesses
   - Give hints whether the guess is too high or too low
   - Example output:
     ```
     I'm thinking of a number between 1 and 100.
     Your guess: 50
     Too high!
     Your guess: 25
     Too low!
     Your guess: 42
     Correct! It took you 3 guesses.
     ```

3. **FizzBuzz**
   - Write a program that prints numbers from 1 to 100
   - For multiples of 3, print "Fizz" instead of the number
   - For multiples of 5, print "Buzz" instead of the number
   - For multiples of both 3 and 5, print "FizzBuzz"
   - Example output:
     ```
     1
     2
     Fizz
     4
     Buzz
     Fizz
     7
     8
     Fizz
     Buzz
     11
     Fizz
     13
     14
     FizzBuzz
     ...
     ```

4. **Pattern Generator**
   - Use nested loops to generate patterns
   - Create at least two different patterns using for loops and range()
   - Example pattern:
     ```
     *
     **
     ***
     ****
     *****
     ```

5. **Simple Calculator**
   - Create a calculator that performs basic operations (+, -, *, /) on two numbers
   - Use if/elif/else to determine which operation to perform
   - Use a while loop to allow multiple calculations
   - Example output:
     ```
     Welcome to Simple Calculator
     
     Enter first number: 10
     Enter operation (+, -, *, /): +
     Enter second number: 5
     10 + 5 = 15
     
     Calculate again? (yes/no): yes
     
     Enter first number: 20
     Enter operation (+, -, *, /): *
     Enter second number: 3
     20 * 3 = 60
     
     Calculate again? (yes/no): no
     Thank you for using Simple Calculator!
     ```



### Nested Loops
You can create nested loops (loops inside loops):

#### Simple multiplication table
```python
print("Multiplication table from 1 to 5:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("---")  # Separator between rows
```

#### Creating a pattern with nested loops
```python
print("Number pattern:")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row
```
Output:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

#### Coordinate grid with nested loops
```python
print("Coordinate grid (x,y):")
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x},{y})", end=" ")
    print()  # New line after each row
```
Output:
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

---

## Resources
- [Python Documentation](https://docs.python.org/3/)
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python For Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python While Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)