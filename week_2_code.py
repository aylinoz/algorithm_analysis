import random

def createRandom(n):
    myarray=[]
    for i in range (n):
        myarray.append(random.randint(0,100))
    return myarray

def bubbleSort(my_array):
    number_of_comparision=0
    for passnum in range(len(my_array)-1,0,-1):
        for i in range(passnum):
            number_of_comparision=number_of_comparision+1
            if my_array[i]>my_array[i+1]:
                temp = my_array[i]
                my_array[i] = my_array[i+1]
                my_array[i+1] = temp
    return (my_array,number_of_comparision)

n=10
for i in range(3):
    print(bubbleSort(createRandom(n)))

n=20
for i in range(3):
    print(bubbleSort(createRandom(n)))
	
n=30
for i in range(3):
    print(bubbleSort(createRandom(n)))
	
n=50
for i in range(3):
    print(bubbleSort(createRandom(n)))
	
	
def insertionSort(alist):
    comparison=0
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index
        comparison=comparison+1
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            comparison=comparison+1
        alist[position]=currentvalue
    return(comparison)
	
n=10
for i in range(3):
    print(insertionSort(createRandom(n)))
	
n=20
for i in range(3):
    print(insertionSort(createRandom(n)))
	
n=30
for i in range(3):
    print(insertionSort(createRandom(n)))
	
n=50
for i in range(3):
    print(insertionSort(createRandom(n)))