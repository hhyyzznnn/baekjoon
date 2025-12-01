# BOJ 13241

import sys
import math
input = sys.stdin.readline

def solve():
    A, B = map(int, input().split())
    print(math.lcm(A, B))

    pass

if __name__ == "__main__":
    solve()