'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.next = None
'''

class Solution:
    def removeDuplicates(self, head):
        temp=head
        while temp != None and temp.next != None:
            if(temp.next.data == temp.data):
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head