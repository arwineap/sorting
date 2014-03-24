#!/usr/bin/env python


import random


# Goal: Implement sorting function using concepts learned from quicksort
def quicksort(n):
    origsort = pivotlist(n)
    newsort = pivotlist(origsort)
    gosort = newsort
    go = True
    i = 0
    while go:
        go1sort = pivotlist(gosort)
        go2sort = pivotlist(go1sort)
        go3sort = pivotlist(go2sort)
        if gosort == go1sort and go1sort == go2sort and go3sort == go2sort:
            print 'winner?'
            go = False
        else:
            print 'gosort', gosort
            print 'go1sort', go1sort
            print 'go2sort', go2sort
            print 'go3sort', go3sort
            gosort = go3sort
        i += 1
    return (gosort, i)

def pivotlist(alist):
    #pivot = alist.pop()
    element = random.randrange(0,len(alist)-1)
    pivot = alist[element]
    alist.remove(alist[element])
    greater = []
    lesser = []
    for entry in alist:
        if entry > pivot:
            greater.append(entry)
        elif entry <= pivot:
            lesser.append(entry)
    #print lesser, pivot, greater
    return lesser + [pivot] + greater


#randomlist = []
#for x in range(1, 10):
#    randomlist.append(random.randrange(1,10))

# disable random list gen, use this one:
randomlist = [8, 6, 6, 1, 6, 5, 6, 8, 2]

print randomlist
randomlist = quicksort(randomlist)
print 'quicksort in %d iterations:' % randomlist[1], randomlist[0]
