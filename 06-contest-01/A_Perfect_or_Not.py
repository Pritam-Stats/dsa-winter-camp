import sys


# Implement only this function.
# Return "Perfect", "Abundant" or "Deficient": compare the sum of the
# proper divisors of n (all its positive divisors except n itself) with n.
def classify(n):
    # pass
    s = 0
    for x in range(1, int(n**(0.5))+1):
        if n%x == 0:
            s += x
            s += (n//x if x != n//x else 0)

    s -= n
    if s == n:
        return "Perfect"
    elif s > n:
        return "Abundant"
    else:
        return "Deficient"




data = sys.stdin.buffer.read().split()
T = int(data[0])

print("\n".join(classify(int(x)) for x in data[1:1 + T]))