def binary_search(nums, target):

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l+r) // 2

        if nums[mid] == target:
            return mid

        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l


print(binary_search([1, 3, 5, 10, 34], 5))
