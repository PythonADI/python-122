import random
import time



game_map = [
    [5, 5, 5, 5, 5],
    [5, 2, 2, 2, 5],
    [5, 5, 5, 5, 5],
]


icons = {
    1: ["🚜"],
    2: ["🟫"],
    3: ["🌱", "🌾"],
    4: ["🌿", "🌳"],
    5: ["🪜"]
}

plant_data = {}
harvested_plants = {
    3: 0,  # Wheat
    4: 0,  # Tree
}
tractor_position = (None, None)


def draw():
    tree_count = harvested_plants[4]
    wheat_count = harvested_plants[3]
    output = f"""Farm Simulator
Time: {time.time()- start_time:.0f}s
Harvested:
🌾: {wheat_count}
"""

    for y, row in enumerate(game_map):
        for x, col in enumerate(row):
            plant = plant_data.get((x, y))
            if plant:
                output += icons[col][plant["stage"]]
                continue

            output += icons[col][0]

        output += "\n"

    print("\x1b[2J\x1b[H", end="")
    print(output)


def is_empty_soil(x, y):
    return game_map[y][x] == 2


def plant_wheat(x, y):
    if is_empty_soil(x, y):
        plant_data[(x, y)] = {
            "time": time.time(),
            "stage": 0,
            "id": 3,
        }
        game_map[y][x] = 3


def plant_tree(x, y):
    if is_empty_soil(x, y):
        plant_data[(x, y)] = {
            "time": time.time(),
            "stage": 0,
            "id": 4,
        }
        game_map[y][x] = 4


def grow_plants():
    for y in range(len(game_map)):
        for x in range(len(game_map[y])):
            if (x, y) in plant_data:
                plant = plant_data[(x, y)]
                elapsed = time.time() - plant["time"]

                if plant["id"] == 3 and plant["stage"] == 0 and elapsed > 5:
                    plant["stage"] = 1
                elif plant["id"] == 4 and plant["stage"] == 0 and elapsed > 10:
                    plant["stage"] = 1


def plant_crops():
    for y, row in enumerate(game_map):
        for x, col in enumerate(row):
            if is_empty_soil(x, y):
                plant_wheat(x, y)
                return


def harvest_crops():
    for y, row in enumerate(game_map):
        for x, col in enumerate(row):
            plant = plant_data.get((x, y))
            if not plant:
                continue
            is_harvestable = plant and plant["stage"] == 1

            if is_harvestable:
                del plant_data[(x, y)]
                game_map[y][x] = 1
                harvested_plants[plant["id"]] += 1
                return x, y
    return None

start_time = time.time()
while True:
    harvested_cell = harvest_crops()
    if harvested_cell:
        if tractor_position[0] is not None:
            game_map[tractor_position[1]][tractor_position[0]] = 2
        tractor_position = harvested_cell
    else:
        if tractor_position[0] is not None:
            game_map[tractor_position[1]][tractor_position[0]] = 2
        tractor_position = (None, None)

    plant_crops()
    grow_plants()
    draw()
    time.sleep(1)

