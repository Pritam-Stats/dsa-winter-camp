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

def cmp(s1, s2):
    if len(s1) < len(s2):
        return -1 
    elif len(s1) > len(s2):
        return 1
    else:
        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
        else:
            return 0

def main():
    n = inp()
    arr = []
    for _ in range(n):
        arr.append(ins())

    # arr.sort(key = lambda x: (len(x), x))
    arr.sort(key=cmp_to_key(cmp))
    for s in arr:
        print_fast(s)


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 