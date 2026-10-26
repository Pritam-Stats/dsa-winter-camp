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

def main():
    n, q = inmap()
    s = ins()
    a = [int(ch) for ch in s]
    # print(a)
    # return
    n = len(a)
    p = [0]*n
    s = 0
    for i in range(n):
        s+= a[i]
        p[i] = s

    for _ in range(q):
        l, r = inmap()
        l-=1
        r -= 1
        rangeSum = (p[r] if l == 0 else p[r] - p[l-1])
        # print(rangeSum)
        interval = r-l+1
        # print(interval)
        if rangeSum*2 == interval:
            print("YES")
        else:
            print("NO")

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        main() 



# import sys







# # Implement only this function.
# # s contains only '0' and '1', and its characters are numbered 1 to n.
# # queries[k] = [L, R] asks whether the substring from character L to
# # character R contains as many zeros as ones.
# # For every query, in order, return whether that substring is balanced.
# def balancedQueries(s, queries):
#     # pass
#     a = [int(ch) for ch in s]
#     # return a
#     n = len(a)
#     p = [0]*n
#     s = 0
#     for i in range(n):
#         s+= a[i]
#         p[i] = s

#     for _ in queries:

# # print(balancedQueries("0110", 0))

# data = sys.stdin.buffer.read().split()
# n, q = int(data[0]), int(data[1])
# s = data[2].decode()
# queries = [[int(data[3 + 2 * k]), int(data[4 + 2 * k])] for k in range(q)]

# print("\n".join("YES" if ok else "NO" for ok in balancedQueries(s, queries)))