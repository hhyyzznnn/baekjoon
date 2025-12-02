# BOJ 1715

from queue import PriorityQueue
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    Q = PriorityQueue()
    S = 0

    for i in range(N):
            Q.put(int(input()))
        
    while not Q.empty():
        s1 = Q.get()
        if Q.empty():
             break
        
        s2 = Q.get()
        S += s1 + s2
        Q.put(s1 + s2)

    print(S)

    pass

if __name__ == "__main__":
    solve()