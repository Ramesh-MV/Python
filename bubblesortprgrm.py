'''
def bubblesort(mylist):
    for i in range(0,len(mylist)-1):
        for j in range(0,len(mylist)-1-i):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                return mylist
mylist=['b','a','c','e','d','f']
print(bubblesort(mylist))
'''

'''
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = ['a','c','b','f','e','d','h','g']
bubbleSort(alist)
print(alist)
'''
'''
def bubblesort(list):
    for k in range(0,len(list)-1,1):
        for i in range(0,len(list)-1,1):
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp

list=[1,4,5,2,3]
bubblesort(list)
print(list)
'''
'''
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[64,44,34,23,11,6,0]
bubblesort(arr)
print('sorted arr is:')
for i in range(len(arr)):
    print("%d" %arr[i])
'''

l = [1,4,2,3,5,6,78,4,9]

for x in range(len(l)):
    swapped = False
    i = 0
    while i<len(l)-1:
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            swapped=True
        i=i+1
    if swapped==False:
        break
print l

