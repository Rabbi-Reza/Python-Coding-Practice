
from array import *

def bubbleSort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        

arr = array('i',[])

n = int(input("Enter array size : "))

for i in range(n):
    
    arrVal = int(input("Enter " + str(i+1)+" element : " )) 
    arr.append(arrVal)
   
print(" Array is : ",arr)

bubbleSort(arr,n)

print("Sorted array is : ",arr)