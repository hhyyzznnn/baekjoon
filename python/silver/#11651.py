# BOJ 11651
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    S = [list(map(int, input().split()))[::-1] for _ in range(N)]
    S.sort()

    for elem in S:
        print(" ".join(map(str, elem[::-1])))
    pass

if __name__ == "__main__":
    solve()