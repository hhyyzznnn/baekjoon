# BOJ 10815
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    set_N = set(map(int, input().split()))
    M = int(input())
    list_M = list(map(int, input().split()))

    for elem in list_M:
        print(int(elem in set_N), end = " ")
    pass

if __name__ == "__main__":
    solve()