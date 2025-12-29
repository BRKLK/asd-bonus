# import sys
# sys.setrecursionlimit(300000)

def merge_sort_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, inv_left = merge_sort_count_inversions(arr[:mid])
    right, inv_right = merge_sort_count_inversions(arr[mid:])

    merge = []
    i = 0
    j = 0

    inv_count = inv_left + inv_right
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            # Все элементы в left[i:] больше чем элемент right[j]]
            inv_count += len(left) - i
            merge.append(right[j])
            j += 1

    merge.extend(left[i:])
    merge.extend(right[j:])

    return merge, inv_count

n = int(input())
arr = [int(el) for el in input().split()]

_, inv_count = merge_sort_count_inversions(arr)
print(inv_count)
# hello
