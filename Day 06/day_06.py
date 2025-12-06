from time import time
from math import prod


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@timer_func
def day06(filepath, part2=False):
    with open(filepath) as fin:
        lines = fin.read().splitlines()
    
    total = 0

    if not part2:
        nums = [[int(x) for x in line.split()] for line in lines[:-1]]
        ops = lines[-1].split()
        for i in range(len(ops)):
            if ops[i] == '+':
                total += sum([nums[x][i] for x in range(len(nums))])
            else:
                total += prod([nums[x][i] for x in range(len(nums))])

        return total
    else:
        rotatedInput = []
        for i in range(len(lines[0])-1,-1,-1):
            num = []
            for x in range(len(lines) - 1):
                num.append(lines[x][i])
            rotatedInput.append("".join(num))
        cpodNums = [[]]
        col = 0
        for x in rotatedInput:
            if not x.isspace():
                cpodNums[col].append(int(x))
            else:
                col += 1
                cpodNums.append([])
        ops = lines[-1].split()[::-1]
        for i, op in enumerate(ops):
            if op == "+":
                total += sum(cpodNums[i])
            else:
                total += prod(cpodNums[i])
        return total


def main():
    assert day06('test06') == 4277673
    print(f"Part 1: {day06('input06')}")

    assert day06('test06', True) == 3263827
    print(f"Part 2: {day06('input06', True)}")


if __name__ == '__main__':
    main()
