import argparse

import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation


HEIGHT = 10  # Height of cells
WIDTH = 10  # Width of cells
INTERVAL = 100  # Interval of animation in milliseconds
FRAMES = 50  # Number of frames in the animation (number of iterations to perform)
OUTPUT_FILE_NAME = "output.gif"  # File name to save (gif file)


# Use parser to get input
parser = argparse.ArgumentParser()
parser.add_argument("--input", dest="input")
args = parser.parse_args()

if args.input:
    with open(args.input) as input:
        cells = [[int(value) for value in line.strip()] for line in input]
else:
    cells = np.random.randint(2, size=(HEIGHT, WIDTH))

# Create a new figure
fig = plt.figure()
# Creating a new full window axes
ax = plt.axes()
# Display an array as a matrix in a new figure window
plot = plt.matshow(cells, fignum=0)


def main():
    """Main function"""
    validate_cells(cells, HEIGHT, WIDTH)
    run_game_of_life_animation(
        file_name=OUTPUT_FILE_NAME, interval=INTERVAL, frames=FRAMES
    )
    print(f"Animation is saved as {OUTPUT_FILE_NAME} file!")


def validate_cells(cells: list, height: int, width: int):
    """Get status of the cell in next generation

    Keyword arguments:
    cells -- The current status of all the cells
    height -- Height of 2-dim cells
    width -- Width of 2-dim cells
    """
    if len(cells) != height:
        raise Exception("Invalid inital configuration")
    for row in cells:
        if len(row) != width:
            raise Exception("Invalid inital configuration")


def trans_to_next_gen(frame_number):
    """Transform all cells to next generation
    The function to call at each frame.

    Keyword arguments:
    frame_number -- Frame number in animation
    """
    # Clone current cells
    current_cells = cells.copy()

    # Update status for each cell
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j] = next_gen_status(i, j, current_cells)
    # Set the image array
    plot.set_data(cells)

    return [plot]


def get_alive_neighbours(x: int, y: int, height: int, width: int):
    """Get number of alive neighbours of the cell

    Keyword arguments:
    x -- X-axis of the cell
    y -- Y-axis of the cell
    height -- Height of 2-dim cells
    width -- Width of 2-dim cells
    """
    result = 0
    for _x in range(x - 1, x + 2):
        for _y in range(y - 1, y + 2):
            if 0 <= _x < height and 0 <= _y < width:
                if not (_x == x and _y == y):
                    # Increase result if cell is alive
                    if cells[_x][_y]:
                        result += 1
    return result


def next_gen_status(x: int, y: int, cells: list):
    """Get status of the cell in next generation

    Keyword arguments:
    x -- X-axis of the cell
    y -- Y-axis of the cell
    cells -- The current status of all the cells
    """
    # Get current cell's status
    cell = cells[x][y]
    # Get number of alive neighbours
    neighbours = get_alive_neighbours(x, y, HEIGHT, WIDTH)

    # Game of life rules
    if cell:
        if neighbours < 2:
            return 0
        elif neighbours == 2 or neighbours == 3:
            return 1
        elif neighbours > 3:
            return 0
    else:
        if neighbours == 3:
            return 1
    return 0


def run_game_of_life_animation(file_name: str, interval: int, frames: int):
    """Run the game and save animation

    Keyword arguments:
    file_name -- File name to save (gif file)
    interval -- Interval in milliseconds
    frames -- Number of frames in the animation (number of iterations to perform)
    """
    ani = animation.FuncAnimation(
        fig,
        trans_to_next_gen,
        interval=interval,
        frames=frames,
        blit=True,
        repeat=False,
    )
    ani.save(file_name)


if __name__ == "__main__":
    main()
