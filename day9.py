from utils import readFile

PREAMBLE_LEN = 25

def checkXMASSum(arr, target, low, high):
    if low < 0 or high >= len(arr) or low > high:
        raise ValueError("Wtf is this nonsense?")
    if low == high:
        return False
    if arr[low] + arr[high] == target:
        return True
    elif arr[low] + arr[high] > target:
        return checkXMASSum(arr, target, low, high-1)
    return checkXMASSum(arr, target, low+1, high)

def isXMASValid(nums, i):
    if i < PREAMBLE_LEN or i >= len(nums):
        raise ValueError("Invalid index {} provided for checking.".format(i))
    subarr = nums[i-PREAMBLE_LEN: i]
    subarr.sort()
    return checkXMASSum(subarr, nums[i], 0, len(subarr)-1)

def findSum(nums, target, start, end):
    if start < 0 or end >= len(nums) or end-start < 1:
        raise ValueError("Invalid start and end indices {} and {} provided".format(start, end))
    s = sum(nums[start:end])
    if nums[end] >= target:
        return findSum(nums, target, end+1, end+2)
    elif s < target:
        return findSum(nums, target, start, end+1)
    elif s > target:
        return findSum(nums, target, start+1, end)
    return start, end

if __name__ == "__main__":
    lines = readFile("data/d9.txt")
    nums = []
    for line in lines:
        nums.append(int(line.strip()))
    target = 0
    for i in range(PREAMBLE_LEN, len(nums)):
        if not isXMASValid(nums, i):
            print("Invalid number is {} at position {}.".format(nums[i], i))
            target = nums[i]
    s, e = findSum(nums, target, 0, 1)
    result = min(nums[s:e]) + max(nums[s:e])
    print("Result is {} on range {} to {}.".format(result, s, e))