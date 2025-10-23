from homework import generate_map, print_map, emojis

game_map = generate_map()


def find_cell_type(search=2):
    print(f"Results of search {emojis[search]}")
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == search:
                print((y, x))


print_map(game_map)
find_cell_type(2)
find_cell_type(1)
