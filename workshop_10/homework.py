import random
import os
import time

# park_map = [
#     ["🟩", "🟦", "🌲"],
#     ["🗻", "🟩", "🟩"],
#     ["🟦", "🌲", "🟩"]
# ]

icons = {
    "🟩": 70, 
    "🌲": 5, 
    "🗻": 5, 
    "🟦": 20
}

emojis = {
    1: '🟩',  # grass
    2: '🟦',  # pond
    3: '🗻',  # hill
    4: '🌲'   # tree
}

# icons_data = []
# for icon, percentage in icons.items():
#     icons_data.extend([icon] * percentage)
    # for _ in range(percentage):
    #     icons_data.append(icon)


def generate_map_emoji(width=3, height=3):
    data_map = []

    for _ in range(height):
        row = random.choices(list(icons.keys()), list(icons.values()), k=width)
        # row = []
        # for _ in range(width):
        #     row.append(random.choice(icons_data))
            

        data_map.append(row)
    
    return data_map

def generate_map(width=3, height=3):
    data_map = []

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(random.randint(1, 4))


        data_map.append(row)
    
    return data_map

# print(park_map)
# print(data_map)



# print("".join(["🟩", "🟦", "🌲"]))
# print("".join(park_map[0]))
# print("🟩🟩🟩\n🟩🟦🟩\n🟩🌲🟩")

def print_map_emoji(park_map):
    for row in park_map:
        print("".join(row))

def print_map(park_map):
    for row in park_map:
        output = ""
        for cell in row:
            output += emojis[cell]
            # print(output)
        print(output)


    
# print_map(park_map)

# while True:
#     os.system("clear")
#     park = generate_map(15, 15)
#     print_map(park)
#     time.sleep(0.1)


# park = generate_map(3, 3)
# print_map(park)