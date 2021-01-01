'''You are given an array 
of distinct integers arr 
and an array of integer arrays 
pieces, where the integers in 
pieces are distinct. Your goal is 
to form arr by concatenating the arrays 
in pieces in any order. However, you are 
not allowed to reorder the integers in 
each array pieces[i].
Return true if it is 
possible to form the array arr from 
pieces. Otherwise, return false.
Edited by Rongxiang
2021 / 1 / 1 
'''

def canFormArray(arr,pieces):

    len_arr = len(arr)
    len_pieces = len(pieces)
    len_pieces_items = []
    for i in pieces:
        len_pieces_items.append(len(i))
    print(len_pieces_items)
    itemlist = []
    for i in range(len_pieces):
        item = pieces[i][0] ##item = 0
        for j in range(len_arr):
            if item == arr[j]:
                alist = []
                for l in range(len_pieces_items[i]):
                    if j + l >= len_arr:
                        arr.append(None)
                    alist.append(arr[j+l])
                itemlist.append(alist)
    return itemlist


    
      
         

arr =[49,18,16]

piecse = [[16,18,49]] 

alist = canFormArray(arr,piecse)
if alist == piecse:
    print("nice")
else:
    print(alist)