# 📝 Python Recap Homework

## **Task 1: Lists**

**Goal:** Practice creating, indexing, slicing, and looping over lists.

**Instructions:**

1. Create a list of 5 products: `"Keyboard"`, `"Mouse"`, `"Monitor"`, `"Speaker"`, `"Webcam"`.
2. Print the first and last product.
3. Add `"Headphones"` to the list.
4. Remove `"Speaker"`.
5. Loop through the list and print each product in uppercase.
6. Print the total number of products in the list.
7. Slice the list to get the first 3 products and print them.
8. Sort the list alphabetically and print it.

---

## **Task 2: Dictionaries**

**Goal:** Practice creating and using dictionaries.

**Instructions:**

1. Create a dictionary for a product:

```python
product = {"name": "Keyboard", "units_sold": 5, "unit_price": 20.0}
```

2. Print the product name and total revenue (`units_sold * unit_price`).
3. Add a new key `"region"` with value `"North"`.
4. Update `"units_sold"` to 10.
5. Loop through the dictionary and print each key and value.
6. Create a list of 3 such product dictionaries with different values.
7. Calculate and print the total revenue for all products in the list.

---

## **Task 3: Strings**

**Goal:** Practice string manipulation.

**Instructions:**

1. Take the string `"Python Programming"`.
2. Print it in lowercase and uppercase.
3. Count how many times `"o"` appears.
4. Replace `"Python"` with `"Java"`.
5. Split the string into a list of words.
6. Join the list back into a single string with a hyphen (`-`) between words.

---

## **Task 4: Conditionals**

**Goal:** Practice if/else statements.

**Instructions:**

1. Ask the user for a number.
2. Print `"Even"` if the number is even, `"Odd"` if it’s odd.
3. Print `"Large"` if the number > 100, `"Small"` otherwise.

---

## **Task 5: Loops**

**Goal:** Practice `for` and `while` loops.

**Instructions:**

1. Create a list of numbers `[2, 4, 6, 8, 10]`.
2. Print each number multiplied by 2 using a `for` loop.
3. Using a `while` loop, print numbers from 1 to 5.

---

## **Task 6: File Handling**

**Goal:** Practice reading and writing files.

**Instructions:**

1. Create a text file `products.txt` with the following content:

```
Keyboard
Mouse
Monitor
Speaker
Webcam
```

2. Write a Python program to:

   * Read the file and print each line.
   * Count the number of products.
   * Add `"Headphones"` to the file.

---

## **Task 7: Final Integrative Task (Lists + Dicts + Strings + Loops + Conditionals + Files)**

**Goal:** Apply all concepts in a small “Store Sales Analysis” project.

**Instructions:**

1. Create a CSV file `sales.csv`:

```
date,product,region,units_sold,unit_price
2025-10-01,Keyboard,North,5,20.0
2025-10-01,Mouse,South,10,15.0
2025-10-02,Keyboard,South,3,21.0
2025-10-02,Monitor,North,2,150.0
2025-10-03,Mouse,North,8,14.5
```

2. Read the CSV file and store data as **list of dictionaries**.
3. Calculate and print:

   * Total units sold for each product.
   * Average unit price per region.
   * Most popular product (highest units sold).
   * Total revenue per region.
4. Filter and print:

   * How many `Keyboard` units were sold in `North`.
   * How many `Mouse` units were sold in `South`.

> Tip: Use loops, conditionals, string methods, type conversion, and dictionaries for aggregations.
