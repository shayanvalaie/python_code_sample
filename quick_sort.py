def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums

    else:
        pivot = nums.pop()

        items_greater = []
        items_lower = []

        for num in nums:
            if num < pivot:
                items_lower.append(num)
            else:
                items_greater.append(num)

        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([4, 2, 6, 8, 23, 20]))
