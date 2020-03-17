def merge_sort(array: list) -> None:
    for (i, item) in enumerate(_merge_sort(array)):
        array[i] = item

def _merge_sort(array: list) -> list:
    avg = len(array)
    if len(array) > 2:
        array[:avg] = _merge_sort(array[:avg])
        array[avg:] = _merge_sort(array[avg:])
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return [array[0], array[1]]
    else:
        return [array[0]]
    i = 0
    k = avg
    result = []
    while i < avg and k < len(array):
        if array[i] < array[k]:
            result.append(array[i])
            i += 1
        else:
            result.append(array[k])
            k += 1
    result[len(array):] = array[i:avg]
    result[len(array):] = array[k:]
    return result