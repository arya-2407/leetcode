def mergeSort(arr,s,e):
    if (e-s) + 1 <= 1:
        return arr
    
    m=(s+e)//2

    mergeSort(arr,s,m)

    mergeSort(arr,m+1,e)

    merge(arr,s,m,e)

    return arr

def merge(arr,s,m,e):
    L=arr[s:m+1]
    R=arr[m+1:e+1]

    i = 0 #tracking left
    j = 0 #tracking right
    k = s #where to insert

    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    while i<len(L):
        arr[k] = L[i]
        k+=1
        i+=1
    
    while j<len(R):
        arr[k] = R[j]
        k+=1
        j+=1

# arr = [18, 9, 10, 11, 17, 2, 13, 16, 8, 14]
# print("Unsorted : ", arr)

# sorted_arr = mergeSort(arr,0,len(arr)-1)
# print("Sorted : ",sorted_arr)


def insertionSort(arr):
    for i in range(len(arr)-1):
        j = i-1
        while j>=0 and arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j-=1
    return arr

# arr = [18, 9, 10, 11, 17, 2, 13, 16, 8, 14]
# print("Unsorted : ", arr)

# sorted_arr = insertionSort(arr)
# print("Sorted : ",sorted_arr)