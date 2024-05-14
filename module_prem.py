import math

def selection(arr1):
    n = len(arr1)
    for i in range(n):
        temp = i
        for j in range(i+1, n):
            if arr1[j] < arr1[temp]:
                temp = j
        arr1[i], arr1[temp] = arr1[temp], arr1[i]

def bubble(arr2):
    n=len(arr2)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr2[j]>arr2[j+1]:
                arr2[j],arr2[j+1]=arr2[j+1],arr2[j]

def insertion(arr3):
    for i in range(1, len(arr3)):
        temp = arr3[i]
        j = i - 1
        while j >= 0 and temp < arr3[j]:
            arr3[j + 1] = arr3[j]
            j = j - 1
        arr3[j + 1] = temp
    return arr3

def shell(arr4):
    n = len(arr4)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = arr4[i]
            j = i
            while j >= interval and arr4[j - interval] > temp:
                arr4[j] = arr4[j - interval]
                j -= interval
            arr4[j] = temp
        k -= 1
        interval = 2**k -1
    return arr4

def heap(arr5, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr5[i] < arr5[l]:
        largest = l
    if r < n and arr5[largest] < arr5[r]:
        largest = r
    
    if largest != i:
        arr5[i], arr5[largest] = arr5[largest], arr5[i]
        heapify(arr5, n, largest)
        
def heapSort(arr5):
    n = len(arr5)
    for i in range(n//2, -1, -1):
        heapify(arr5, n, i)
    for i in range(n-1, 0, -1):
        arr5[i], arr5[0] = arr5[0], arr5[i]
        heapify(arr5, i, 0)
    return arr5

def merge(arr6):
    if len(arr6)==1:
        return arr6
    mid = (len(arr6)-1) // 2
    lst1 = mergeSort(arr6[:mid+1])
    lst2 = mergeSort(arr6[mid+1:])
    result = mergeSort(lst1, lst2)
    return result
def mergeSort(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst

def quick(arr7):
    if len(arr7)> 1:
        pivot=arr7.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in arr7:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quick(smlr_lst) + equal_lst + quick(grtr_lst))
    else:
        return arr7

def count(arr8):
    M = max(arr8)
    count_array = [0] * (M + 1)
    for num in arr8:
        count_array[num] += 1
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
    output_array = [0] * len(arr8)
 
    for i in range(len(arr8) - 1, -1, -1):
        output_array[count_array[arr8[i]] - 1] = arr8[i]
        count_array[arr8[i]] -= 1
 
    return output_array


def radixSort(arr9, place):
    size = len(arr9)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        index = arr9[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = arr9[i] // place
        output[count[index % 10] - 1] = arr9[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        arr9[i] = output[i]

def radix(arr9):
    max_element = max(arr9)
    place = 1
    while max_element // place > 0:
        radixSort(arr9, place)
        place *= 10

arr=[64,34,25,12,22,11,90]
count(arr)
print(arr)
