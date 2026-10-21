# n = 6
# arr = [1,2,3,4,5,6]




# # for l in range(n):
# #     for r in range(l, n):
# #         print(arr[l:r+1])



# # for l in range(n):
# #     summ = 0
# #     for r in range(l, n):
# #         summ += arr[r]
# #         print(summ, end=" ")
# #     print()


# # max of each subarray

# arr = [7, 3, 9, 1]


# for l in range(len(arr)):
#     mx = arr[l]
#     for r in range(l, len(arr)):
#         mx = max(mx, arr[r])
#         print(mx, end = " ")
#     print()

        
## TOTAL SUM OF ALL SUBARRAYS

a = [1, 2, 4,6, 9]
n = len(a)
ans = 0
for l in range(n):
    s = 0
    for r in range(l, n):
        s+= a[r]
        ans += s
#on2
        
# print(ans)

## ps
a = [1, 2, 4,6, 9]
n = len(a)

#visualize the pattern col wise
# O(n)
def totalSubarraySum(arr, n):
    totalSum = 0
    for i in range(n):
        totalSum += a[i]*(n-i)*(i+1)
    return totalSum

print(totalSubarraySum(a, n))
    






