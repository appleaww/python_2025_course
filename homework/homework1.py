def maxArea(nums):
    left=0
    right = len(nums) - 1
    res = 0

    while left < right:
        width = right - left
        if nums[left] < nums[right]:
            height = nums[left]
            left += 1
        else:
            height = nums[right]
            right -= 1
        tmp = width * height
        if tmp > res:
            res = tmp

    return res

nums = [6, 1, 8, 1, 3, 1]
print(maxArea(nums))
nums = [2, 1, 8, 1, 3, 1]
print(maxArea(nums))