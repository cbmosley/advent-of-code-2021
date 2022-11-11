import sys
from pathlib import Path

higherdepth = []


def DepthIncreases(input):
    depthint = input.split()
    nums = [eval(i) for i in depthint]
    total = 0
    for i in range(0, len(nums)):
        if nums[i] > nums[i - 1]:
            total += 1
    print(total)
    # take text file given in input.txt


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        DepthIncreases(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
