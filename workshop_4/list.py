import datetime

temperatures = [-7, -8, -9, -11, -14, -14, -14, -13, -10, -9]
print(len(temperatures))
print(temperatures)

start_date = datetime.date(2025, 5, 18)

s = 0
for i, temp in enumerate(temperatures):
    print(f"{start_date.strftime('%d/%m/%Y (%A)')}: {temp}")
    start_date += datetime.timedelta(days=1)
    s += temp

print(s)
avg = s / len(temperatures)
print(f"Average temperature according to our journal is: {avg}")
