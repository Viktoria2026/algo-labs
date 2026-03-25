def quickselect(arr, k):
    if len(arr) < k or k <= 0:
        raise ValueError("Некоректне значення k")

    def select(left, right, k_smallest):
        pivot = arr[right]
        p = left

        for i in range(left, right):
            if arr[i] <= pivot:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1

        arr[p], arr[right] = arr[right], arr[p]

        if p == k_smallest:
            return arr[p]
        elif p < k_smallest:
            return select(p + 1, right, k_smallest)
        else:
            return select(left, p - 1, k_smallest)

    n = len(arr)
    return select(0, n - 1, n - k)






