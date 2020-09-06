#!/user/bin/env pypy3
import sys
from typing import List


def fast_input():
    return sys.stdin.readline()[:-1]


def is_all_even(nums: List[int]) -> bool:
    for n in nums:
        if n % 2 == 1:
            return False
    return True


def solve(n: int, nums: List[int]) -> int:
    manipulate_count = 0
    while is_all_even(nums):
        manipulate_count += 1
        nums = list(map(lambda x: int(x / 2), nums))
    return manipulate_count


def main():
    n = int(fast_input())
    a = list(map(int, fast_input().split()))
    result = solve(n, a)
    print(result)


main()
