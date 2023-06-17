import sys
def position(arr):
    largest = arr[0]
    pos = 1
    for i in range(0, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            pos = i + 1
    return pos
if __name__ == '__main__':
    a = input()
    arr = map(int, input().split())
    print(position(list(arr)))