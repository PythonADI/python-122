```markdown
# 📝 Workshop 12 — Homework 10

## Overview

This homework continues practicing object-oriented programming and working with classes, files and simple data processing. You'll build small classes, use inheritance, and read/write CSV data.

## Task 1: Classes & Instances

Goal: Practice defining classes, __init__, methods and properties.

Instructions:

1. Create a class `Product` with attributes: `name` (str), `unit_price` (float), `units_sold` (int, default 0).
2. Add a method `revenue()` that returns `unit_price * units_sold`.
3. Add a `__str__` method that returns `"{name}: {units_sold} units at ${unit_price:.2f}"`.
4. Instantiate three `Product` objects and print them and their revenues.

---

## Task 2: Inheritance

Goal: Practice creating subclasses and overriding methods.

Instructions:

1. Create a subclass `PerishableProduct(Product)` with an extra attribute `expiry_date` (string "YYYY-MM-DD").
2. Override `__str__` to include expiry date.
3. Add a method `is_expired(today)` that returns True/False comparing date strings (you can compare lexicographically for this exercise).
4. Create one instance and demonstrate `is_expired` with two example dates.

---

## Task 3: CSV Processing (Integrate OOP + Files)

Goal: Read product sales from a CSV, map to `Product` / `PerishableProduct`, and produce simple summaries.

Instructions:

1. Use the provided `workshop_12/products_sample.csv` (or create a small CSV) with columns: `name,region,unit_price,units_sold,expiry_date` (expiry_date may be empty for non-perishables).
2. Read the CSV and create either `Product` or `PerishableProduct` objects depending on `expiry_date` presence.
3. Calculate and print:
   - Total revenue across all products.
   - Revenue per region.
   - The product with the highest revenue.
4. Save a new CSV `workshop_12/products_summary.csv` with the columns: `name,region,units_sold,unit_price,revenue,expired` (expired should be `True/False` for perishables; `False` for non-perishables).

---

## Task 4: Extra (Optional)

1. Add command-line arguments so the script can accept input and output CSV paths.
2. Add simple unit tests for `revenue()` and `is_expired()`.

---

Submit: a Python file `workshop_12/homework_10.py` (or a small package) and the generated `products_summary.csv` if you run it locally.

Tips: Keep functions small, add helpful print statements, and include a `if __name__ == "__main__"` example run.
```
