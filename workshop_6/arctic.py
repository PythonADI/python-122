temperatures = [-15, -16, -17, -16.5, -16.7, -17.1, -15.3, -15, 32, 33]

print(f"We recorded {len(temperatures)} days of data")
temperatures.append(7)
temperatures.insert(len(temperatures) // 2, -17)

if len(temperatures) % 2 == 0:
    print("We have 2 numbers in the middle so: ")
    print(temperatures[(len(temperatures) // 2) - 1])
    print(temperatures[len(temperatures) // 2])
else:
    print(temperatures[len(temperatures) // 2])


s = 0
for i, temperature in enumerate(temperatures, start=1):
    print(f"Day {i}: {temperature}")
    s += temperature

print(f"Sum = {s}")
avg = s / len(temperatures)
print(f"AVG = {round(avg, 4)}")


print(f"{sum(temperatures) / len(temperatures):.4f}")
