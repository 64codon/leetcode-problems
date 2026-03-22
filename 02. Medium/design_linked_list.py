class Node:
    def __init__(self, initdata=0, next=None):
        self.data = initdata
        self.next = next

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.end = None

    def get(self, index: int) -> int:
        current = self.head
        step = 0
        
        while current is not None and step != index:
            current = current.getNext()
            step += 1
        
        # Check if the number of steps is equivalent to the given index
        if step == index:
            # If current is None, fetch the datafield of the last node
            if current is None:
                temp = self.end
                return temp.getData()
            # Otherwise, return the datafield of the current node
            else:
                return current.data
        
        

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp

        # Check if the list was initially empty
        # If so, add a reference to your end pointer along with your head pointer
        if self.end is None:
            self.end = self.head
        

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        current = self.end

        if current is not None:
            current.setNext(temp)
        else:
            # i.e. The list is empty
            self.end = temp
            self.head = self.end

    def addAtIndex(self, index: int, val: int) -> None:
        prev = None
        current = self.head
        step = 0

        while current is not None and step != index:
            current = current.getNext()
            step += 1
        
        # Is the current pointer referencing the first node in the list?
        if prev is None:
            self.addAtHead(val)
        # Is the previous pointer referencing the last node in the list?
        elif current is None:
            prev.setNext(temp)
        # Is the index equal to the size of the lsit?
        # If so, add the node at the end of the list
        elif index == step + 1:
            self.addAtTail(val)
        # Are the prev and current pointers referencing two valid nodes in the list?
        else:
            temp = Node(val)
            temp.setNext(current)
            prev.setNext(temp)

    def deleteAtIndex(self, index: int) -> None:
        prev = None
        current = self.head
        step = 0

        while current is not None and step != index:
            current = current.getNext()
            step += 1

        if current is None:
            return
        elif prev is None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)