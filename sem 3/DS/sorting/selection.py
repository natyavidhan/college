nums = [5, 3, 6, 7, 2, 9, 10, 14, 4]

for i in range(len(nums)):
    shortest = i
    for j in range(i+1, len(nums)):
        if nums[j] < nums[shortest]:
            shortest = j
    nums[i], nums[shortest] = nums[shortest], nums[i]

print(nums)