from time import time
from bisect import bisect_right

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
def day05(filepath, part2=False):
    with open(filepath) as fin:
        lines = [line.strip() for line in fin.readlines()]

    blank_id = lines.index('')
    range_lines = [[int(y) for y in x.split('-')] for x in lines[:blank_id]]
    id_lines = [int(x) for x in lines[blank_id+1:]]

    range_lines.sort()
    # merge the ranges
    merged_ranges = [range_lines[0]]
    for s, e in range_lines[1:]:
        l_s, l_e = merged_ranges[-1]
        if s <= l_e + 1:
            merged_ranges[-1][1] = max(l_e, e)
        else:
            merged_ranges.append([s, e])

    fresh_count = 0
    starts = [s for s, _ in merged_ranges]
    if not part2:
        for i in id_lines:
            id_m = bisect_right(starts, i) - 1
            if id_m >= 0:
                s, e = merged_ranges[id_m]
                if s <= i <= e:
                    fresh_count += 1
    else:
        for s,e in merged_ranges:
            fresh_count += e - s + 1
    return fresh_count


def main():
    assert day05('test05') == 3
    print(f"Part 1: {day05('input05')}")

    assert day05('test05', True) == 14
    print(f"Part 2: {day05('input05', True)}")


if __name__ == '__main__':
    main()
