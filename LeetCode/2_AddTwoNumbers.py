'''
Question Link: https://leetcode.com/problems/add-two-numbers/

Linked List: https://www.youtube.com/watch?v=JlMyYuY1aXU&t=302s&ab_channel=BrianFaure
'''

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        newNode = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode

    def length(self):
        current = self.head
        total = 0 

        while current.next != None:
            total += 1
            current = current.next
        return total
    
    def display(self):
        elems = []
        currentNode = self.head
        while currentNode.next!= None:
            currentNode = currentNode.next
            elems.append(currentNode.val)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        
        currentIndex = 0
        currentNode = self.head

        while True:
            currentNode = currentNode.next
            if currentIndex == index: return currentNode.val
            currentIndex += 1

    def erase(self,index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        
        currentIndex = 0
        currentNode = self.head

        while True:
            lastNode = currentNode
            currentNode = currentNode.next

            if currentIndex == index:
                lastNode.next = currentNode.next
                return
            currentIndex += 1

def linkListCreate(data):
    linkedList = LinkedList()
    for elem in data:
        linkedList.append(elem)
    
    return linkedList.head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    # Brute Force Solution
    def addTwoNumberBF(self, l1:Node, l2:Node):
        dummy = Node()
        current = dummy

        carrier = 0
        while l1 or l2 or carrier:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carrier
            carrier = val // 10
            val = val % 10
            current.next = Node(val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy
    # HashMap - 1
    

    # HashMap - Best



l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

linkedList1 = linkListCreate(l1)
linkedList2 = linkListCreate(l2)

SolutionObj = Solution()

resultNode = SolutionObj.addTwoNumberBF(linkedList1.next,linkedList2.next)

elems = []
# currentNode = resultNode.head
while resultNode.next!= None:
    resultNode = resultNode.next
    elems.append(resultNode.val)
print(elems)