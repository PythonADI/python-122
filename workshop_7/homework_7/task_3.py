import datetime


# today = datetime.date(2025, 10, 16)
# today = datetime.datetime.now()
# start_date = datetime.datetime(1970, 1, 1)

# days_gone = today.timestamp() / 3600 / 24 / 365
# print(today.timestamp())
# print(days_gone)
# print(start_date - today)



def is_valid_fromat(date_str):
    data = date_str.split(" ")
    if len(data) != 3:
        return False
    year, month, day = data
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False
    
    month = int(month)
    if month < 1 or 12 < month:
        return False

    day = int(day)
    if day < 1 or 31 < day:
        return False
    
    return datetime.datetime.strptime(date_str, "%Y %m %d")



print(is_valid_fromat("2026 12 17"))
print(is_valid_fromat("2026 29 31"))
print(is_valid_fromat("2026 12 31"))
print(is_valid_fromat("Hello 29 31"))
print(is_valid_fromat("2029 ni 31"))
print(is_valid_fromat("2029 12 3na1"))
