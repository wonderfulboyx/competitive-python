#!/user/bin/env pypy3
import sys
from typing import Tuple


def fast_input():
    return sys.stdin.readline()[:-1]


def solve(num: int, amount: int) -> Tuple[int, int, int]:
    for count_10000 in range(0, num + 1):
        for count_5000 in range(0, num - count_10000 + 1):
            count_1000 = num - (count_10000 + count_5000)
            total = count_10000 * 10000 \
                        + count_5000 * 5000 \
                        + count_1000 * 1000
            if total == amount:
                return count_10000, count_5000, count_1000
    return -1, -1, -1


def main():
    n, y = list(map(int, fast_input().split()))
    result = solve(n, y)
    print(*result)


main()
