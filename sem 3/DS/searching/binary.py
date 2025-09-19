import random
nums = [1, 4, 6, 7, 8, 10, 11, 14, 20]

search =11
start = 0
end = len(nums) - 1

def binary(n, start, end):
    mid_point = (start + end) // 2
    print(n[start:end], mid_point)
    mid_val = n[mid_point]
    
    if search == mid_val:
        return mid_point
    if mid_val > search:
        return binary(n, start, mid_point - 1)
    elif mid_val < search:
        return binary(n, mid_point + 1, end)
    
    
print(binary(nums, start, end))