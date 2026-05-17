def findCount(arr, num, diff):
    count = 0

    for i in arr:
        if abs(i - num) <= diff:
            count += 1

    if count == 0:
        return -1

    return count

arr = [12, 3, 14, 56, 77, 13]

print(findCount(arr, 13, 2))
