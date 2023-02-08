class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None # tail is the last node whoose next=None 
        self.size=0

    def traverse(self,):
        point=self.head
        ll=[]
        while point:
            ll.append(point.val)
            point=point.next
        print(ll)

    def get(self, n: int) -> int:
        if n<self.size and n>=0 and self.size !=0:
            target_node=self.head
            for i in range(n):
                if target_node.next:
                    target_node=target_node.next
            get_val= target_node.val
        else:
            get_val= -1
        return get_val

    def addAtHead(self, val: int) -> None:
        new_node=ListNode(val)
        if self.head==None: 
            # means this will be the very first element of the list
            # for the very first element:
            # first make the new element as the head node
            # then, make the tail and head be the same
            self.head=new_node
            self.tail=self.head
        else:
            new_node.next=self.head
            self.head=new_node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        new_node=ListNode(val)
        if self.head==None: # means this will be the very first element of the list
            self.head=new_node
            self.tail=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1

    def addAtIndex(self, n: int, val: int) -> None:
        if n==0:            # Handling adding at head
            self.addAtHead(val)
        elif n==self.size:  # Handling adding at tail
                            # generally the maximum value of n should be self.size-1
                            # but, if n==self.size : that means, 
                            # nth element will be the extra element added at the very last as the new tail
            self.addAtTail(val)
        elif n>0 and n<self.size:
            newNode=ListNode(val)
            target_node=self.head
            prev_node=ListNode()
            for i in range(n): # n is using 0-indexed numbering
                prev_node=target_node
                target_node=target_node.next
            prev_node.next=newNode
            newNode.next=target_node
            self.size+=1

    def deleteAtIndex(self, n: int) -> None:
        if n==0 and self.size>0:    # Handling deleting the head node
            self.head=self.head.next
            self.size-=1
        elif self.size >1 and n<self.size: # Handling the ideal cases + deleting tail node
            prev_node=None
            target_node=self.head
            for i in range(n): # n is using 0-indexed numbering
                prev_node=target_node
                target_node=target_node.next
            if self.size==n+1:   # Handling deleting the tail node
                prev_node.next=None
                self.tail=prev_node
            else:                # Handling the ideal cases: deleting an element from the middle of the list 
                prev_node.next=target_node.next
            self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)