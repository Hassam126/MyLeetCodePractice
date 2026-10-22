# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
       
        a = l1
        b = l2
        dummy = ListNode(0)
        c = dummy
        carry = 0
        
        while a is not None and b is not None:
            t = a.val+b.val+carry 

            if t>=0 and t<=9:
               carry = 0
               new_node= ListNode(t)
              
            elif t>=10 and t<=19:
                v = t%10
                carry = 1
                new_node = ListNode(v)
            c.next = new_node
            c = c.next

            a = a.next
            b = b.next         

        while a is not None:
            t1 = a.val + carry
            if t1>=0 and t1<=9:
                carry = 0
                new_node= ListNode(t1)
                  
            else:
                v = t1%10
                carry = 1
                new_node = ListNode(v)

            c.next = new_node
            c = c.next   
            a = a.next
                                 
        while b is not None:
            t1 = b.val + carry
            if t1>=0 and t1<=9:
                carry = 0
                new_node= ListNode(t1)
               
            else:
                v = t1%10
                carry = 1
                new_node = ListNode(v)

            c.next = new_node
            c = c.next      
            b = b.next    
        if carry == 1:
            
           new_node = ListNode(1)   
           c.next = new_node
           c = c.next  

        return dummy.next 
        