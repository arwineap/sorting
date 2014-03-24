#!/usr/bin/env python


import random


# Goal: Implement sorting function using concepts learned from quicksort
def pivotalist(alist):
    element = random.randrange(0, len(alist)-1)
    pivot = alist[element]
    greater = []
    lesser = []
    pivotList = []
    for entry in alist:
        if entry > pivot:
            greater.append(entry)
        elif entry < pivot:
            lesser.append(entry)
        else:
            pivotList.append(entry)
    resultList = lesser + pivotList + greater
    return resultList

#randomlist = [5, 6, 3, 2, 1, 4, 7, 10, 9, 8]
#randomlist = [8, 6, 6, 1, 6, 5, 6, 8, 2]

randomlist = []
for x in range(1, 10000):
    randomlist.append(random.randrange(1, 10000))

matchX = 0
count = 0
a = pivotalist(randomlist)
while matchX != 10:
    c = a
    b = pivotalist(a)
    if b == a:
        matchX += 1
    else:
        a = b
    count += 1

print "it took %d iterations to sort this list of %d entries" % (count, len(randomlist))
#print a
