#!/usr/bin/py


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
	
array = [3,2,10,9,5,7]

sorted_array = bubbleSort(array)

print(sorted_array)