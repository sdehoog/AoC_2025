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


def caret_positions(s: str) -> list[int]:
    return [i for i, ch in enumerate(s) if ch == '^']


@timer_func
def day07(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    splitters = [set(caret_positions(line)) for line in lines[1:]]
    split_count = 0

    beams = [{lines[0].index("S"): 1}]
    for line in splitters:
        b_s = set(beams[-1].keys())
        split = b_s.intersection(line)
        not_split = b_s.difference(line)
        if split:
            beams.append({})
            for b in split:
                split_count += 1
                for s in b-1, b+1:
                    if s in beams[-1]:
                        beams[-1][s] += beams[-2][b]
                    else:
                        beams[-1][s] = beams[-2][b]
            if not_split:
                for b in not_split:
                    if b in beams[-1]:
                        beams[-1][b] += beams[-2][b]
                    else:
                        beams[-1][b] = beams[-2][b]

    return sum(beams[-1].values()) if part2 else split_count


def main():
    assert day07('test07') == 21
    print(f"Part 1: {day07('input07')}")

    assert day07('test07', True) == 40
    print(f"Part 2: {day07('input07', True)}")


if __name__ == '__main__':
    main()
