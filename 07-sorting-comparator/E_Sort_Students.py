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
    ## i need two students to compare
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        if a[0] < b[0]:
            return -1
        if a[0] > b[0]:
            return 1
        else:
            return 0

def main():
    n = inp()
    students = []
    for _ in range(n):
        name, marks = input().split()
        students.append((name, int(marks)))

    # students.sort(key= cmp_to_key(cmp))
    students.sort(key= lambda s : (-s[1], s[0]))
    for tups in students:
        print_fast(*tups)



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 