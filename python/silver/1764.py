# BOJ 1764

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    set_N = {input().strip() for _ in range(N)}
    set_M = {input().strip() for _ in range(M)}

    set_Ins = set_N & set_M

    print(len(set_Ins))

    for elem in sorted(list(set_Ins)):
        print(elem)
    
    pass

if __name__ == "__main__":
    solve()