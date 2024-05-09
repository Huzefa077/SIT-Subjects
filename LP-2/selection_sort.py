#selection sort
def selection_sort(arr1):
    for i in range (len(arr1)-1):
        # small = i
        for j in range (i+1,len(arr1)):
            if arr1[i] > arr1[j]:
                arr1[i],arr1[j]=arr1[j],arr1[i]
    return arr1
                
arr1 = [12,10,99,11,25]
selection_sort(arr1)
print("sorted array = ")
for i in range (len(arr1)):
    print(arr1[i])
print("The array was sorted using selection sort algorithm")