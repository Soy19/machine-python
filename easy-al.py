num = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
def binary_search(num, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value
            left = mid + 1
        else:
            right = mid - 1
            return -1           

num = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(binary_search(num, 90))
