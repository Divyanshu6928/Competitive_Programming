# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    #Return the number of critical points (integer)
    c=0
    if(head.next==None):
        return 0
    new=head.next
    old=head.val
    while(new.next !=None):
        if((old > new.val and new.next.val > new.val) or (old < new.val and new.next.val < new.val)):
            c+=1
        old=new.val
        new=new.next
    return c
            
    
    