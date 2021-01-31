# # game of life
# # rules
#
# * Any live cell with fewer than two live neighbors dies (underpopulation).
# * Any live cell with two or three live neighbors continues to live.
# * Any live cell with more than three live neighbors dies (overpopulation).
# * Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

import random
import time
from hashlib import sha256

statuses = [0, 0, 0, 1]  #  0.25 of the grid will start live


def build_canvas(row_num: int, col_num: int) -> list:
    canvas = []
    for i in range(0, row_num):
        row_list = []
        for j in range(0, col_num):
            row_list.append(random.choice(statuses))
        canvas.append(row_list)

    return canvas


def get_cell_properties(row_value: int, col_value: int) -> tuple:
    live = canvas[row_value][col_value]

    canvas_height = len(canvas)
    canvas_width = len(canvas[0])

    # count neighbours
    count = 0

    first_col = True if col_value == 0 else False
    last_col = True if col_value == canvas_width - 1 else False
    first_row = True if row_value == 0 else False
    last_row = True if row_value == canvas_height - 1 else False

    if not first_row and not first_col:
        count += canvas[row_value - 1][col_value - 1]
    if not first_row:
        count += canvas[row_value - 1][col_value]
    if not first_row and not last_col:
        count += canvas[row_value - 1][col_value + 1]

    if not first_col:
        count += canvas[row_value][col_value - 1]
    if not last_col:
        count += canvas[row_value][col_value + 1]

    if not last_row and not first_col:
        count += canvas[row_value + 1][col_value - 1]
    if not last_row:
        count += canvas[row_value + 1][col_value]
    if not last_row and not last_col:
        count += canvas[row_value + 1][col_value + 1]

    return live, count


def run_cycle(canvas_input: list) -> list:
    buffer = canvas  # make a list of lists to update
    for i in range(0, len(canvas)):
        # print(f'row is {i}')
        for j in range(0, len(canvas[1])):
            # print(f'col is {j}')
            cell_properties = get_cell_properties(i, j)
            if cell_properties[0] == 1:  # cell is alive
                if cell_properties[1] < 2:
                    status = 0
                elif cell_properties[1] > 3:
                    status = 0
                else:
                    status = 1
            elif cell_properties[0] == 0:  # cell is dead
                if cell_properties[1] == 3:
                    status = 1
                else:
                    status = 0

            # print(f'was {cell_properties[0]} now {status}')
            buffer[i][j] = status  # set the status of the cell in the buffer

    return buffer


canvas = build_canvas(15, 15)
seen_again = 0

while seen_again < 10:
    # for i in range(0, 500):
    this_hash = sha256(str(canvas).encode("utf-8")).hexdigest()

    run_cycle(canvas)

    next_hash = sha256(str(canvas).encode("utf-8")).hexdigest()
    if next_hash == this_hash:
        seen_again += 1
    else:
        seen_again = 0
    this_hash = next_hash

    for row in canvas:
        row = ["*" if x == 1 else " " for x in row]
        print("".join(row))
        # print("".join(str(row)).replace("0", " ").replace("1", "X"))

    # time.sleep(0.1)
    print("\033c")  # clear console
