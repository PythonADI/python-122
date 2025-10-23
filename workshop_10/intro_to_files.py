"""
What is a file?
What properties do files have?
How do we read from and write to files in Python?

- File is a container in a computer system for storing data or information.
- Files have properties such as name, size, type, location (path), and permissions.
    - Name: The name of the file (e.g., data.txt).
    - Size: The amount of data stored in the file (e.g., 15 KB)
    - Type: The format of the file (e.g., text file, binary file, CSV file).
    - Location (Path): The directory or folder where the file is stored (e.g., /home/user/documents/data.txt).
    - Permissions: The access rights for the file (e.g., read, write, execute).
- In Python, we can read from and write to files using built-in functions like open(), read(), write(), and close().
- We can also use context managers (with statement) to handle files more efficiently and safely.
"""
# import os
import pprint
import datetime

pth = "workshop_10/data.csv"

# print(os.path.exists(pth))


data = []

# print(f.read())
def read_as_dict(pth):
    f = open(pth)

    headers = f.readline().strip().split(",")
    print(headers)
    for line in f.readlines():
        row = line.strip().split(",")
        row_data = {}
        for i, header in enumerate(headers):
            cell = row[i]
            if header == "date":
                cell = datetime.datetime.strptime(cell, "%Y-%m-%d").date()
            elif header == "units_sold": 
                cell = int(cell)
            elif header == "unit_price":
                cell = float(cell)

            row_data[header] = cell
        data.append(row_data)

    f.close()
    return data

data = read_as_dict(pth)
pprint.pprint(data)

s = 0
count = 0

for sale in data:
    if sale["product"] == "Keyboard" and sale["region"] == "North":
        s += sale["units_sold"]
        count += 1

print(f"Total sold: {s}")
print(f"Average: {s / count}")

