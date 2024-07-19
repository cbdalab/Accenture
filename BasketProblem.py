# n = 5
n = int(input())
# k = 3
k = int(input())
# arr = [9, 2, 5, 3, 7]
arr = list(map(int, input().split(" ")))
ans = 0

for i in range(n - k + 1):
    sub_arr = arr[i:i + k]
    sum = 0
    for j in range(1, k + 1):
        sum += sub_arr[j - 1] * j
    if sum > ans:
        ans = sum
        
print(ans)
