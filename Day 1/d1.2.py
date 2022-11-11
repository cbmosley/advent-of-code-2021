import sys
from pathlib import Path


def three_measure(input):
    group_add = input.split()
    nums = [eval(i) for i in group_add]
    window_size = 3
    count = 0
    for i in range(len(nums) - window_size + 1):
        if sum(nums[i: i + window_size]) < sum(nums[i + 1: i + window_size + 1]):
            count += 1
        # print(sum(nums[i: i + window_size]))
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        three_measure(Path.read_text(file))
    else:
        raise TypeError("This is not a file")
