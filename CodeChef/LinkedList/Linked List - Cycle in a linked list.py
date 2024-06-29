'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    def detectCycle(self, head):
        #code here
        if(head==None and head.next==None):
            return 0
        else:
            s=head
            f=head
            while(f!=None or f.next!=None):
                s=s.next
                f=f.next.next
                
                if(s==f):
                    s=head
                    
                    while(s!=f):
                        s=s.next
                        f=f.next
                        
                    return s
            return None
            
