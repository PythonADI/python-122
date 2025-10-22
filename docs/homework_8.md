# Homework 8: Fun with Functions and Maps!

## Welcome!
Let's practice Python functions by building and exploring a fun 2D map. Each task is broken into easy steps, with hints and examples. You can use code from `workshop_7` for help.

---

### 1. Create a Pet Park Map
- Write a function to make a 2D grid (list of lists) with any number of rows and columns.
- Each cell should randomly be one of these areas: `'grass'`, `'pond'`, `'hill'`, `'tree'`.
- Use emojis for each area: `'grass'` = '🟩', `'pond'` = '🟦', `'hill'` = '🏔️', `'tree'` = '🌲'.
- HINT: Use the `random` module and `random.choice()`.
- Write another function to print the map nicely.
- Example for a 3x3 map:
```
🟩🟦🌲
🏔️🟩🟩
🟦🌲🟩
```
- Try changing the size and see what happens!

---

### 2. Numeric Map to Emoji Map
- Make a dictionary:
```python
emojis = {
    1: '🟩',  # grass
    2: '🟦',  # pond
    3: '🏔️',  # hill
    4: '🌲'   # tree
}
```
- Write a function to make a grid with numbers (1-4) instead of emojis.
- Let the user choose the width and height. Example: `generate_map(width, height)`.
- Write a function to turn the number map into an emoji map and print it.
- Example:
```python
game_map = [
    [1, 2, 4],
    [3, 1, 1],
    [2, 4, 1]
]
```
Prints:
```
🟩🟦🌲
🏔️🟩🟩
🟦🌲🟩
```
- HINT: Use loops and the `emojis` dictionary.

---

### 3. Find a Type of Area
- Write a function to search the map for a specific number (e.g., 2 for pond).
- Return a list of coordinates (row, column) where you find it.
- Example: Searching for ponds (2) might return: `Found pond at: (0, 1), (2, 0)`
- HINT: Use nested loops and `enumerate()`.

---

### 4. Planting Game!
- Make a grid for a farm, with empty cells as '🟫'.
- Let the user "plant" crops (e.g., '🌽' for corn) by entering row and column numbers.
- After each planting, show the updated farm.
- HINT: Use `input()` and loops.
- Example after planting:
```
🟫🟫🟫🟫
🟫🌽🌽🟫
🟫🟫🟫🟫
🟫🟫🌽🟫
```
- Try adding your own crop emoji!

---

## Bonus: Be Creative!
- Add your own area or crop types and emojis.
- Try making a bigger map, or a map with obstacles.
- Share your favorite map with a friend!

---

## Tips
- Use comments to explain your code.
- Test each function with different inputs.
- Ask for help if you get stuck—coding is teamwork!
