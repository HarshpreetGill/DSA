from typing import List

def selection_sort(arr: List[int], n: int):
    for i in range(n-1):
        min_index = i #sorting from the start
        for j in range(i+1, n): #traverse whole array
            if arr[min_index]>arr[j]:
                min_index = j 
        arr[min_index], arr[i] = arr[i], arr[min_index]
        
    for i in range(n):
        print(arr[i], end=' ')
        
arr_input = input("enter cs elemets for array: ").strip()
if arr_input:
    arr = list(map(int, arr_input.split(',')))
    n = len(arr)
    selection_sort(arr,n)
else:
    print("no input found")
