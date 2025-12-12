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


def get_factors(n: int) -> list[int]:
    """
    Return all factors of n (excluding n itself).
    """
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i and n // i != n:
                factors.append(n // i)
    return sorted(factors)


@timer_func
def day02(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    ranges = [x.split('-') for x in lines[0].split(',')]
    id_sum = 0

    for s, e in ranges:
        s, e = int(s), int(e)
        for i in range(s, e + 1):
            i = str(i)
            if not part2:
                if len(i) % 2 == 0:
                    half = len(i) // 2
                    if i[:half] == i[half:]:
                        id_sum += int(i)
            else:
                factors = get_factors((len(i)))
                for n in factors:
                    ss = i[:n]
                    cs = ss * (len(i) // n)
                    if cs == i and (len(i) // n) > 1:
                        print(cs, i)
                        id_sum += int(i)
                        break
    return id_sum


def main():
    assert day02('test02') == 1227775554
    print(f"Part 1: {day02('input02')}")

    assert day02('test02', True) == 4174379265
    print(f"Part 2: {day02('input02', True)}")


if __name__ == '__main__':
    main()
