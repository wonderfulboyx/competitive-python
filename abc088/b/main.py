#!/user/bin/env pypy3
import sys
from typing import List


def fast_input():
    return sys.stdin.readline()[:-1]


def solve(cards: List[int]) -> int:
    sorted_cards = sorted(cards, reverse=True)
    alice = 0
    bob = 0
    for i, card in enumerate(sorted_cards):
        if i % 2 == 0:
            alice += card
        else:
            bob += card
    return alice - bob


def main():
    n = int(fast_input())
    a = list(map(int, fast_input().split()))
    result = solve(a)
    print(result)


main()
