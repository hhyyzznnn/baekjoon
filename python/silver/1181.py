# BOJ 1181
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    S = []
    for i in range(N):
        I = input().strip()
        S.append((len(I), I))
    S = set(S)
    S = list(S)
    S.sort()

    for elem in S:
        print(elem[1])
    pass

if __name__ == "__main__":
    solve()