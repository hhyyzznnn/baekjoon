# BOJ 10814
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    S = []
    
    for i in range(N):
        age, name = input().split()
        S.append((int(age), i, name))
    S.sort()
    
    for elem in S:
        print(str(elem[0]) + " " + elem[2])
    pass

if __name__ == "__main__":
    solve()