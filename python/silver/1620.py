# BOJ 1620
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    dict_name = {}
    dict_num = {}

    for i in range(N):
        name = input().strip()
        dict_name[name] = i + 1
        dict_num[i + 1] = name

    list_M = [input().strip() for _ in range(M)]

    for elem in list_M:
        if elem.isdigit():
            print(dict_num[int(elem)])
        else:
            print(dict_name[elem])

    pass

if __name__ == "__main__":
    solve()