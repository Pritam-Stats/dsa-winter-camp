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
from dataclasses import dataclass

@dataclass
class Students:
    name: str
    marks: int


def cmp(a, b):
    if a.marks != b.marks:
        return b.marks - a.marks
    return (a.name > b.name) - (a.name < b.name)

def main():
    n = inp()
    students = []
    for _ in range(n):
        name, marks = input().split()
        students.append((Students(name, int(marks))))

    students.sort(key= cmp_to_key(cmp))
    for s in students:
        print_fast(f"{s.name} {s.marks}")



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 