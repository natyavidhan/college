nums = [5, 3, 6, 7, 2, 9, 10, 14, 4]
end = len(nums) - 1

for end_ in range(end, 0, -1):
    for i in range(0, end_):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            
print(nums)
    