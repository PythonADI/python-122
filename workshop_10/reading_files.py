import pprint
import datetime
df = {}

with open("workshop_10/data.csv") as f:
    headers = f.readline().strip().split(",")
    for header in headers:
        df[header] = []
    
    for line in f.readlines():
        for i, cell in enumerate(line.strip().split(",")):
            # print(i, cell)
            header = headers[i]

            if header == "date":
                cell = datetime.datetime.strptime(cell, "%Y-%m-%d").date()
            elif header == "units_sold": 
                cell = int(cell)
            elif header == "unit_price":
                cell = float(cell)
            df[header].append(cell)



# pprint.pprint(df)

print(sum(df["units_sold"]))
print(sum(df["units_sold"]) / len(df["units_sold"]))

