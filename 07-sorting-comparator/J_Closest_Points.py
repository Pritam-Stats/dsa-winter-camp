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
class Ref:
    x: int
    y: int

@dataclass
class Ordinates:
    x: int
    y: int


def main():
    n, a, b = inmap()
    ref = Ref(a, b)
    points:Ordinates = []
    for _ in range(n):
        x, y = inmap()
        points.append(Ordinates(x, y))


    def euclidean_distance(ref:Ref, point: Ordinates):
        d = (ref.x - point.x)**2 + (ref.y - point.y)**2
        return d

    def cmp(p1:Ordinates, p2:Ordinates):
        d1 = euclidean_distance(ref, p1)
        d2 = euclidean_distance(ref, p2)
        if d1 != d2:
            return d1 - d2
        elif p1.x != p2.x:
            return p1.x - p2.x
        else:
            return p1.y - p2.y

    points.sort(key = cmp_to_key(cmp))

    for p in points:
        print_fast(f"{p.x} {p.y}")

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 