def quick_sort(array: list) -> None:
    _quick_sort(array, 0, len(array) - 1)

def _quick_sort(array, min_index, max_index):
    i = min_index
    k = max_index
    # Hoare's partition
    pivot = array[(min_index + max_index) // 2]
    while i <= k:
        while array[i] < pivot and i < max_index: i += 1
        while array[k] > pivot and k > min_index: k -= 1
        if i <= k:
            array[i], array[k] = array[k], array[i]
            i += 1
            k -= 1
    if min_index < k: _quick_sort(array, min_index, k)
    if i < max_index: _quick_sort(array, i, max_index)