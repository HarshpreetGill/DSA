def insertion_sort(arr: list[int], n: int):
    for i in range(n):
        j = i
        # saari kahaani while ki 
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    for i in range(n):
        print(arr[i], end=' ')
arr_input = input("enter cs elemets for array: ").strip()
if arr_input:
    arr = list(map(int, arr_input.split(',')))
    n = len(arr)
    insertion_sort(arr,n)
else:
    print("no input found")
        
        