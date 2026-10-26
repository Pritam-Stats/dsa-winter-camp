import sys

from collections import Counter
# Implement only this function.
# Return the number of pairs (l, r) with 0 <= l <= r < n and
# colours[l] == colours[r]. A piece made of a single bead counts.
def countPrettyPieces(colours):
    # pass
    n = len(colours)
    cnt = n
    for l in range(n-1):
        for r in range(l+1, n):
            if colours[l] == colours[r]:
                cnt += 1
    return cnt




data = sys.stdin.buffer.read().split()
n = int(data[0])
colours = [int(x) for x in data[1:1 + n]]

print(countPrettyPieces(colours))