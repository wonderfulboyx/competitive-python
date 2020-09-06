import sys


def fast_input():
    return sys.stdin.readline()[:-1]


def solve(a, b):
    product = a * b
    if product % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    a, b = map(int, fast_input().split())
    result = solve(a, b)
    print(result)


main()
