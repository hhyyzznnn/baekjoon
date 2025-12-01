# BOJ 7785
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    dict_N = {}
    list_enter = []

    for i in range(N):
        name, IO = input().split()
        dict_N[name] = IO
    for key, value in dict_N.items():
        if value == "enter":
            list_enter.append(key)

    list_enter.sort(reverse = True)
    print("\n".join(list_enter))

    pass

if __name__ == "__main__":
    solve()