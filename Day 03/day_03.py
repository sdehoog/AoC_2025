from time import time


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


def max_joltage(bank: str, k: int = 12) -> int:
    """
    Given a string of digits (bank), select exactly k digits
    to form the largest possible number while preserving order.
    """
    stack = []
    to_remove = len(bank) - k  # how many digits we can drop

    for digit in bank:
        # While we can remove digits and the current digit is larger
        # than the last one in the stack, pop from stack
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # If we still have digits to remove, trim from the end
    result = stack[:k]
    return int("".join(result))


def total_output_joltage(banks: list[str], k: int = 12) -> int:
    """
    Compute the total output joltage across all banks.
    """
    return sum(max_joltage(bank, k) for bank in banks)


@timer_func
def day03(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    batteries = lines
    if not part2:
        joltage = 0
        for b in batteries:
            first = max(b[:-1])
            f_i = b.index(first) + 1
            second = max(b[f_i:])
            joltage += int(first + second)
        return joltage
    return total_output_joltage(batteries)


def main():
    assert day03('test03') == 357
    print(f"Part 1: {day03('input03')}")

    assert day03('test03', True) == 3121910778619
    print(f"Part 2: {day03('input03', True)}")


if __name__ == '__main__':
    main()
