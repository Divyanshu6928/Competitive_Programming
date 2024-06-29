"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def getMiddleElement(head):
    l=0
    el=head
    while el is not  None:
        l+=1
        el=el.next

    mid_index=l//2
    
    el=head
    for _ in range(mid_index):
        el=el.next
      
    return el.data    
    