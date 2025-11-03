from settings import BASE_DIR

data_path = BASE_DIR / "workshop_11" / "data.txt"

with open(data_path, "a") as f:
    for i in range(10000):
        f.write(f"\nthis is appended line {i}\n")

