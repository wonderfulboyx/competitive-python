#!/user/bin/env pypy3
import sys
from typing import List


def fast_input():
    return sys.stdin.readline()[:-1]


def print_format(b: bool) -> str:
    return "YES" if b else "NO"


def solve(s: str, tokens: List[str], dp_max: int) -> bool:
    dp = [False] * dp_max
    dp[0] = True

    for s_ind in range(len(s)):
        if not dp[s_ind]:
            continue
        for token in tokens:
            if s[s_ind:s_ind + len(token)] == token:
                dp[s_ind + len(token)] = True
    return dp[len(s)]


def main():
    tokens = ["dream", "erase", "eraser", "dreamer"]
    s = fast_input()
    result = solve(s=s, tokens=tokens, dp_max=len(s) + 6)
    print(print_format(result))


main()
