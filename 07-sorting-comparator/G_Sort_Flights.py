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
class Flight:
    number: int
    departureTime: int
    destination: str 

def cmp(a: Flight, b: Flight):
    ##two flights
    if a.departureTime != b.departureTime:
        return a.departureTime - b.departureTime
    ##else smaller flight number
    return a.number - b.number



def main():
    n = inp()
    flights:Flight = []
    for _ in range(n):
        number, departureTime, destination = ins().split()
        flights.append(Flight(int(number), int(departureTime), destination))
    flights.sort(key=cmp_to_key(cmp))

    for fl in flights:
        print_fast(f"{fl.number} {fl.departureTime} {fl.destination}")

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 