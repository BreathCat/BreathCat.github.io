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

    def allitem(self):
        cur = self.head
        while cur is not None:
            yield cur.coef,cur.exp
            cur = cur.next

    def add(self,coef,exp):
        node = Node(coef,exp)
        node.next = self.head
        self.head = node

    def append(self, coef,exp):
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
            self.add(coef,exp)
        elif index >self.length():
            return "index>length"
        else:
            node = Node(coef,exp)
            cur = self.head
            for i in range(1,index-2):
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
            self.append(num[i], num[i + 1])

def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(type(a[1]), a, "\n")
    print(type(b[1]), b, "\n")
    ListA = SingleLinkList()
    ListB = SingleLinkList()
    ListA.getvalue(a)
    ListB.getvalue(b)

'''4 3 4 -5 2  6 1  -2 0
3 5 20  -7 4  3 1'''
if __name__ == '__main__':
    main()





