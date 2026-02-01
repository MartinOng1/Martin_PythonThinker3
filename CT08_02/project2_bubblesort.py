l1=[9, 6, 3, 25, 21, 8, 23, 1, 17, 14]
l2=[37, 39, 41, 29, 9, 25, 43, 21, 3, 42]
l3=[24, 8, 10, 22, 45, 34, 28, 39, 3, 32]
l4=[15, 21, 8, 32, 46, 44, 37, 20, 27, 22]
l5=[11, 38, 4, 28, 24, 41, 15, 10, 45, 14]

l6=[1, 3, 4, 8, 14, 17, 32, 41, 44, 45]
l7=[6, 13, 15, 17, 18, 34, 41, 40, 44, 46]
l8=[18, 22, 23, 26, 27, 34, 36, 37, 44, 47]
l9=[3, 7, 8, 16, 45, 31, 20, 22, 14, 23]

def bubblesort(mylist):
    for i in range(len(mylist) - 1):
        for j in range(len(mylist) - i - 1):
            if mylist[j] < mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist

def checkasc(mylist):
    asc = True
    for i in range(len(mylist) - 1):
        for j in range(len(mylist) - i - 1):
            if mylist[j] > mylist[j+1]:
                return False
    return asc

#task 2
print(bubblesort(l1))
print(bubblesort(l2))
print(bubblesort(l3))
print(bubblesort(l4))
print(bubblesort(l5))

#task 1
print(checkasc(l6))
print(checkasc(l7))
print(checkasc(l8))
print(checkasc(l9))