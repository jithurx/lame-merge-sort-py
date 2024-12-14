def listsplit(inlist): # splits the list recursively 
    if len(inlist) <=1:
        return inlist
    mid = len(inlist)//2
    a=inlist[:mid]
    b=inlist[mid:]
    outlist=mergelist(listsplit(a),listsplit(b))
    return outlist

def mergelist(a,b): # merge 2 sorted list in ascending order of their element
    sortl = []
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            sortl.append(a.pop(0))
        elif a[0]>b[0]:
            sortl.append(b.pop(0))
        else:
            sortl.extend([a.pop(0),b.pop(0)])
    if len(a)>len(b):
        sortl.extend(a)
    elif len(a)<len(b):
        sortl.extend(b)
    return sortl

def cleanlist(inlist):# removes the junk
    junk = []
    for com in range(0,len(inlist)):
        if not (isinstance(inlist[com],int) or isinstance(inlist[com],float)) :
            junk.append(inlist.pop(com))
    return inlist,junk

def mergesort(inlist,order=1,clean=1): # main function
    xlist,junk = cleanlist(inlist)
    nlist=listsplit(xlist)
    if order == 2:
        nlist=nlist[::-1]
    if clean== 0:
        nlist.extend(junk)
    return nlist