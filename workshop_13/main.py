import datetime
from pathlib import Path


class Product:
    def __init__(self, name, region, price, unit_sold):
        self.name = name
        self.region = region
        self.price = price
        self.unit_sold = unit_sold


    def __str__(self):
        return f"{self.name} - {self.price}"


class PerishableProduct(Product):
    def __init__(self, name, region, price, unit_sold, expiry_date):
        super().__init__(name, region, price, unit_sold)
        self.expiry_date = expiry_date
    
    def __str__(self):
        return f"{self.name} - {self.price} - {self.expiry_date}"


def parse_line_to_product(row):
    values = row.strip().split(",")
    values[2] = float(values[2])
    values[3] = int(values[3])
    if values[4]:
        values[4] = datetime.datetime.strptime(values[4], "%Y-%m-%d")
        return PerishableProduct(*values)
    print(values)
    return Product(*values[:4])


products = []

BASE_DIR = Path(__file__).parent.parent
PRODUCTS_FILE = BASE_DIR / "workshop_12" / "products_sample.csv"
print(PRODUCTS_FILE)

with open(PRODUCTS_FILE) as f:
    f.readline()

    for line in f.readlines():
        product = parse_line_to_product(line)
        products.append(product)


for product in products:
    print(type(product), product)
        