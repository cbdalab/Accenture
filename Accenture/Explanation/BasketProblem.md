# Basket Problem 

***Question***

You are competing in a basketball contest. In this contest the score for
each successful shot depends on both the distance from the basket and
the player's position. The ball is shot N times, successfully. You are
given an array A containing the distance of a player from basket for N
shots. The index of array represents the position of the player. Score
is calculated by multiplying the position with the distance from the
basket.

Your task is to find and return an integer value, representing the
maximum possible score you can achieve by choosing a contiguous subarray
sof size K from the given array.

>**Note**:

>A subarray is a contiguous part of array.

>Assume 1 based indexing.

>The array contains both negative and positive values.

>Assume the player is standing on a cartesian plane.

### Input Format

- **input1**: An integer value N representing the number of shots made by
the player
- **input2**: An integer K representing the size of subarray
- **input3**: An array of integers

### Sample Input 1:

```python
N = 5
K = 2
#distance values: 
1 2 3 4 5
#index values:    
1 2 3 4 5
```
### Sample output 1:
```bash
14
```

### Sample Input 2:

```python
n = 5
k = 3
#distance values: 
9 2 5 3 7
#index values:    
1 2 3 4 5
```
### Sample output 3:
```bash
32
```

## Solution :

```python
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
```

[../Problems/BasketProblem.py](click here for python file)