#!/usr/bin/env python

import random

def bubblesort(alist):
    xmatch = 0
    count = 1
    taint = 0
    while xmatch < 1:
        for i in range(0, len(alist)-1):
            if i == len(alist)-count:
                pass
            else:
                if alist[i] > alist[i+1]:
                    newi = alist[i+1]
                    newi1 = alist[i]
                    alist[i] = newi
                    alist[i+1] = newi1
                    taint = 1
        if taint == 0:
            xmatch += 1
        else:
            xmatch = 0
        count += 1
        taint = 0
    return (alist, count)


#randomlist = [5, 6, 3, 2, 1, 4, 7, 10, 9, 8]
randomlist = []
for x in range(1, 10000):
    randomlist.append(random.randrange(1, 10000))


result = bubblesort(randomlist)
print "bubblesort finished sorting %d elements in %d iterations" % (len(result[0]), result[1])