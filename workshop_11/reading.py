from settings import BASE_DIR

print(f"{BASE_DIR = }")
print(f"{__file__ = }")


# folders = __file__.split("/")
# folders[-1] = "data.txt"

# print("/".join(folders))


# data_path = "./workshop_11/files.py"
data_path = BASE_DIR / "workshop_11" / "data.txt"

print(data_path)

with open(data_path, "r") as f:
    print(f.read())

