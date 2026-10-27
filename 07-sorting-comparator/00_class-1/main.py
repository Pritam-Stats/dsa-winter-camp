from functools import cmp_to_key

## unlike cpp python expects a int return in key
## cmp to srt based on last digit
def cmp(a, b):
    # return a%10 < b%10
    lastA, lastB = a%10, b%10
    if lastA < lastB:
        return -1
    elif lastA > lastB:
        return 1
    else:
        #equal
        if a>b:
            return 1
        else:
            return -1



a = [12, 54, 1, 3, 69, 70, 85]
b = [5, 75, 25, 54, 1, 3, 69, 70, 85]
a.sort(key=cmp_to_key(cmp))
print(a)
b.sort(key=cmp_to_key(cmp))
print(b)