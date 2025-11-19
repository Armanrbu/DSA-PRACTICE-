def bubble_sort(arr):
    n = len(arr)

    # har pass me biggest element end me chala jata hai
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            # agar current element bada hai next se, swap kar do
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # agar koi swap hi nahi hua, array already sorted hai
        if not swapped:
            break

    nums = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(nums)
    print("Sorted:", nums)

