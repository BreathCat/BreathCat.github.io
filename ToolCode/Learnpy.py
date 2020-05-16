#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Node(object):
    def __init__(self,coef,exp):
        self.coef = coef
        self.exp = exp
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def show_all(self):
        print(self.length(),' ')
        cur = self.head
        while cur:
            print(cur.coef, ' ', cur.exp, ' ')
            cur = cur.next

    def allitem(self):
        cur = self.head
        while cur is not None:
            yield cur.coef,cur.exp
            cur = cur.next

    def add(self,coef,exp):
        node = Node(coef,exp)
        node.next = self.head
        self.head = node

    def append(self,coef,exp):
        node = Node(coef,exp)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node


    def insert(self,coef,exp,index):
        if index < 0:
            return("index error")
        elif index >self.length():
            self.append(coef,exp)
        else:
            node = Node(coef,exp)
            cur = self.head
            for i in range(index-2):
                cur = cur.next
            node.next = cur.next
            cur.next = node



    def remove(self,data):
        cur = self.head
        if self.head is None:
            return None
        if self.head.item == data:
            self.head = None
        for i in range(1,self.length()):
            if cur.next.item == data:
                cur = cur.next.next

    def getvalue(self,num=None):
        for i in range(1, 2 * num[0] + 1, 2):
            node = Node(num[i], num[i + 1])
            self.append(num[i], num[i + 1])

def addlink(ListA:SingleLinkList, ListB:SingleLinkList)-> SingleLinkList:
    curA = ListA.head
    curB = ListB.head
    OutPutList = SingleLinkList()
    if curA is None:
        return ListB
    elif curB is None:
        return ListA
    while curA and curB :
        if curA.exp == curB.exp:
            OutPutList.append(curA.coef + curB.coef,curA.exp)
            curA = curA.next
            curB = curB.next
        elif curA.exp > curB.exp:
            OutPutList.append(curA.coef,curA.exp)
            curA = curA.next
        elif curA.exp < curB.exp:
            OutPutList.append(curB.coef,curB.exp)
            curB = curB.next

    if curA :
        cur = OutPutList.head
        while cur.next is not None:
            cur = cur.next
        cur.next = curA
    elif curB:
        cur = OutPutList.head
        while cur.next is not None:
            cur = cur.next
        cur.next = curB


    return OutPutList

def multilink(ListA:SingleLinkList,ListB:SingleLinkList) -> SingleLinkList:
    curA = ListA.head
    OutPutLinkList = SingleLinkList()
    while curA:
        curB = ListB.head
        CurLinkList = SingleLinkList()
        while curB:
            CurLinkList.append(curA.coef * curB.coef, curA.exp + curB.exp)
            curB = curB.next
        CurLinkList.show_all()
        OutPutLinkList = addlink(OutPutLinkList, CurLinkList)
        curA = curA.next
    return OutPutLinkList

'4 3 4 -5 2  6 1  -2 0'
'3 5 20  -7 4  3 1'
def main():
    a = [4, 3, 4, -5, 2,  6, 1,  -2, 0]
    b = [3, 5, 20, -7, 4, 3, 1]
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    ListA = SingleLinkList()
    ListB = SingleLinkList()
    ListA.getvalue(a)
    ListB.getvalue(b)
    AddList = addlink(ListA,ListB)
    MultiList = multilink(ListA, ListB)
    MultiList.show_all()




'''4 3 4 -5 2  6 1  -2 0
3 5 20  -7 4  3 1'''
if __name__ == '__main__':
    main()





