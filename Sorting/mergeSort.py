def mergeSort(arr,s,e):
    #base case
    if e-s+1 <= 1:
        return arr
    
    m = (s+e)//2

    #split left
    mergeSort(arr,s,m)

    #split right
    mergeSort(arr,m+1,e)

    #merge
    merge(arr,s,m,e)

    return arr

#inplace merge
def merge(arr,s,m,e):
    L = arr[s:m+1]
    R = arr[m+1:e+1]
    
    i = 0 #tracks left array
    j = 0 #tracks right array
    k = s #tracks where to put element in original array

    #compare leftmost elements of left and right
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    #remaining left arr elements
    while i<len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    
    #remaining right arr elements
    while j<len(R):
        arr[k] = R[j]
        j+=1
        k+=1

arr = [18, 9, 10, 11, 17, 2, 13, 16, 8, 14]
print("Unsorted : ", arr)

sorted_arr = mergeSort(arr,0,len(arr)-1)
print("Sorted : ",sorted_arr)
