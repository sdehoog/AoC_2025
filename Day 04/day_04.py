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
def day04(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]



    return 0


def main():
    assert day04('test04') == 1
    print(f"Part 1: {day04('input04')}")

    # assert day04('test04', True) == 1
    # print(f"Part 2: {day04('input04', True)}")


if __name__ == '__main__':
    main()
