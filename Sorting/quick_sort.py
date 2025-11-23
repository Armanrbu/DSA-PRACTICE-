def quick_sort(arr, low, high):
    # base condition
    if low >= high:
        return

    # partition array and get pivot index
    pivot_index = partition(arr, low, high)

    # sort left part
    quick_sort(arr, low, pivot_index - 1)
    # sort right part
    quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # taking last element as pivot (simple and common)
    pivot = arr[high]
    i = low - 1  # pointer for smaller elements

    for j in range(low, high):
        # if current element is smaller/equal than pivot
        if arr[j] <= pivot:
            i += 1
            # swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot at correct position
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


    nums = [10, 7, 8, 9, 1, 5]
    # important: pass 0 and len(nums) - 1
    quick_sort(nums, 0, len(nums) - 1)
    print("Sorted:", nums)
