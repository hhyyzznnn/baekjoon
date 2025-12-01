# BOJ 1934

import sys
import math
input = sys.stdin.readline

def solve():
    T = int(input())
    A = [0] * T
    B = [0] * T

    for i in range(T):
        A[i], B[i] = map(int, input().split())
    for i in range(T):
        print(math.lcm(A[i], B[i]))
    
    pass

def solve2():
    T = int(input())
    A = [0] * T
    B = [0] * T

    for i in range(T):
        A[i], B[i] = map(int, input().split())
    for i in range()

    pass

if __name__ == "__main__":
    solve()