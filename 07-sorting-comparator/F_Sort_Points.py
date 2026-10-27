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

from dataclasses import dataclass
from functools import cmp_to_key

@dataclass
class Coordinates:
    x: int
    y: int

def cmp(p1, p2):
    if p1.x != p2.x:
        return p1.x - p2.x
    return p1.y - p2.y


def main():
    n = inp()
    points = []
    for _ in range(n):
        x, y = inmap()
        # points.append((x, y))
        points.append(Coordinates(x, y))

    # points.sort(key= lambda p: (p[0], p[1]))
    points.sort(key=cmp_to_key(cmp))
    for p in points:
        print_fast(f"{p.x} {p.y}")


# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 