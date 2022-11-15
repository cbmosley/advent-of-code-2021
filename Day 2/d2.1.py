import sys
from pathlib import Path
import numpy as np
# with open('test-input-two.txt', 'r') as function:
#     lines = function.readlines()


def DepthIncrease(input):
    horizontal_pos, depth = 0, 0
    list = input.split()
    coordinates = np.array(list).reshape(-1, 2).tolist()
    for i in range(0, len(coordinates), 1):
        direction = str(coordinates[i][0])
        magnitude = int(coordinates[i][1])
        if "forward" == direction:
            horizontal_pos += magnitude
        elif "down" == direction:
            depth += magnitude
        elif "up" == direction:
            depth -= magnitude
    print(horizontal_pos, depth)
    print(horizontal_pos * depth)


# file intake
if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        DepthIncrease(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
