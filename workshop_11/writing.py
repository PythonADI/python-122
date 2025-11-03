from settings import BASE_DIR

data_path = BASE_DIR / "workshop_11" / "data.txt"

print(BASE_DIR)
with open(data_path, "w") as f:
    f.write("Hello\nthis\nis\nfrom\npython file") 
