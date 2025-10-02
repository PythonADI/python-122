for i in range(1, 10):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        print(f"I found it! {i}")
        break
