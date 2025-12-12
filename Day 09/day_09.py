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


@timer_func
def day09(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    points = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines]
    largest_area = 0
    for i, p1 in enumerate(points):
        for p2 in points[i:]:
            dx = abs(p1[0] - p2[0]) + 1
            dy = abs(p1[1] - p2[1]) + 1
            area = dx * dy
            if area > largest_area:
                largest_area = area

    return largest_area


def main():
    assert day09('test09') == 50
    print(f"Part 1: {day09('input09')}")

    # assert day09('test09', True) == 1
    # print(f"Part 2: {day09('input09', True)}")


if __name__ == '__main__':
    main()
