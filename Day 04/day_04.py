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


def neighbors8(point):
    """
    Given a point (x, y), return a set of the 8 surrounding (x, y) points.
    """
    x, y = point
    return {
        (x - 1, y - 1),
        (x,     y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x,     y + 1),
        (x + 1, y + 1),
    }


@timer_func
def day04(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    paper_rolls = set()
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == '@':
                paper_rolls.add((x, y))

    if not part2:
        a_count = 0
        for roll in paper_rolls:
            if len(neighbors8(roll).intersection(paper_rolls)) < 4:
                a_count += 1

        return a_count
    else:
        start_rolls = len(paper_rolls)
        while True:
            r2r = set()
            for roll in paper_rolls:
                if len(neighbors8(roll).intersection(paper_rolls)) < 4:
                    r2r.add(roll)
            if len(r2r) == 0:
                return start_rolls - len(paper_rolls)
            paper_rolls.difference_update(r2r)


def main():
    assert day04('test04') == 13
    print(f"Part 1: {day04('input04')}")

    assert day04('test04', True) == 43
    print(f"Part 2: {day04('input04', True)}")


if __name__ == '__main__':
    main()
