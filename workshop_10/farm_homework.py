import os
emojis = {
    1: "🟫",
    2: "🌽"
}

def generate_farm(width=3, height=3):
    data_map = []

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(1)

        data_map.append(row)
    
    return data_map


def print_map(park_map):
    for row in park_map:
        output = ""
        for cell in row:
            output += emojis[cell]
            # print(output)
        print(output)


farm = generate_farm()

while True:
    print("\033[2J")
    print_map(farm)
    x, y = input("x, y: ").split(",")
    x = int(x.strip())
    y = int(y.strip())


    is_in_boundaries = y > len(farm) or x > len(farm[0])
    if is_in_boundaries:
        continue
    farm[y][x] = 2
