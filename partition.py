sample = [14, 5, 8, 64, 7, 54, 15]


def partition(sample, start, end):
    print("sample=", sample)
    pivot = sample[end]
    index = start
    current = start
    while (current < end):
        if (sample[current] <= pivot):
            sample[index], sample[current] = sample[current], sample[index]
            index += 1
        current += 1
    sample[end], sample[index] = sample[index], sample[end]
    print("partitioned=", sample)
    return index


def quickSort(sample, start, end):
    if (start < end):
        index = partition(sample, start, end)
        quickSort(sample, start, index - 1)
        quickSort(sample, index + 1, end)


quickSort(sample, 1, 4)
