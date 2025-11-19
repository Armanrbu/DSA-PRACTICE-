def merge_sort(arr):
    # array size 1 ya 0 hai toh already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # left aur right half sort kar lo
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # ab merge karna hai
    return merge(left, right)


def merge(left, right):
    i = j = 0
    result = []

    # dono arrays ko compare karke sorted form banate jao
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # agar left/right me kuch bacha ho toh directly chipka do
    result.extend(left[i:])
    result.extend(right[j:])

    return result

    nums = [12, 11, 13, 5, 6, 7]
    sorted_nums = merge_sort(nums)
    print("Sorted:", sorted_nums)
