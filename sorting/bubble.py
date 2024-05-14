def bubble_sort(arr: list[int], n: int):
    for i in range(n-1,0, -1): #sorting from the end
        for j in range(i):
            if arr[j]>arr[j+1]:  # bubble
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(n):
        print(arr[i], end=' ')
        
arr_input = input("enter cs elemets for array: ").strip()
if arr_input:
    arr = list(map(int, arr_input.split(',')))
    n = len(arr)
    bubble_sort(arr,n)
else:
    print("no input found")
