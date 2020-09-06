#!/user/bin/env pypy3
import sys


def fast_input():
    return sys.stdin.readline()[:-1]


def solve(masus: str):
    masu_list = map(int, list(masus))
    bdama_count = 0
    for masu in masu_list:
        if masu == 1:
            bdama_count += 1
    return bdama_count


def main():
    result = solve(fast_input())
    print(result)


main()
