# BOJ 18870
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    L1 = list(map(int, input().split()))

    L2 = set(L1)
    L2 = sorted(list(L2))
    
    D = {}

    for i in range(len(L2)):
        D[L2[i]] = i
    
    for elem in L1:
        print(str(D[elem]), end = " ")
    print("n")

    pass

if __name__ == "__main__":
    solve()