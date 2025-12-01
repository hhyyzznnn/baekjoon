# BOJ 10816
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    list_N = list(map(int, input().split()))
    M = int(input())
    list_M = list(map(int, input().split()))
    
    dict_N = {}

    for elem in list_N:
        if elem in dict_N.keys():
            dict_N[elem] += 1
        else:
            dict_N[elem] = 1

    for elem in list_M:
        if elem in dict_N.keys():
            print(dict_N[elem], end = " ")
        else:
            print(0, end = " ")
    
    pass

if __name__ == "__main__":
    solve()