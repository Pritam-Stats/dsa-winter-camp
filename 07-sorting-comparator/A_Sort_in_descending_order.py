# ================================
# Author: Pritam
# ================================


import sys
input = sys.stdin.readline
# ---------- Helpers ----------
def ceil(a, b):    ##relation b/w floor division and ceil division
    return (a+b-1)//b
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def ins():
    return input().strip()
def inmap():
    return map(int, input().split())
def print_fast(*args):
    sys.stdout.write(" ".join(map(str, args)) + '\n')
# ---------- Solve Function ----------


from functools import cmp_to_key
def cmp(a, b):
    # if a>b:
    #     return -1     #return -1 if you want a to come
    # else:
    #     return 1
    return b-a


def main():
    n = inp()
    arr = inlt()
    arr.sort(key=cmp_to_key(cmp))
    print(' '.join(map(str, arr)))



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 