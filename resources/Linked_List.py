from itertools import count
from locale import currency
from os import curdir


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):   
        new_node = Node(data)
        #empty linked list case
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  #self.head is a node which will have a pointer to the next element 
            last_node = last_node.next
        last_node.next = new_node
    
    def printl(self):
        itr = self.head
        while itr:
            print(str(itr.data) + '-+-', end=' ')
            itr = itr.next
        

    def prepend(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_after(self,index,value):
        itr = self.head
        for i in range(index):
            itr_bi = itr
            itr = itr.next
        new_node = Node(value)
        new_node.next = itr
        itr_bi.next = new_node
    
    def del_value(self,val):
        if val == self.head.data:
            self.head = self.head.next
        else:
            itr = self.head
            while itr.data:
                if str(itr.next.data) == val:
                    prev_itr =  itr
                    prev_itr.next = itr.next.next
                    break
                itr = itr.next

    def delete_node(self, key):   #Another method to delete the node
  
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next 
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next 

        if cur_node is None:
            return 
        
        prev.next = cur_node.next
        cur_node = None
    
    def index(self,index):
        itr = self.head
        if index >= 0:
            for i in range(index):
                itr = itr.next 
            if itr == None:
                print('Index out of Range')
            else:
                return itr.data
        else:
            print('Not defined for negative index')

    def del_at_index(self,index):
        curr_node = self.head
        index_element = self.index(index)
        if index == 0:
               self.head = curr_node.next 
        else:
            for i in range(index):
                if curr_node.next.data == index_element:
                    prev_index_element = curr_node
                    break
                curr_node = curr_node.next
            prev_index_element.next = prev_index_element.next.next 
            # index_element.next = None

    def delete_node_at_pos(self, pos):   #Another method to Delete node at a index
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None
    
    def length(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count+=1
            curr_node = curr_node.next
        return count

    def len_recursive(self, node): #recursive method to find length of linked list
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def node_swap(self,n1,n2):
        prev_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.data == n1:
                n1_curr_node = curr_node
                n1_prev_node = prev_node
            if curr_node.data == n2:
                n2_curr_node = curr_node
                n2_prev_node = prev_node
                break
            prev_node = curr_node
            curr_node = curr_node.next
        n1_prev_node.next.data,n2_prev_node.next.data =  n2_curr_node.data,n1_curr_node.data
        # n2_prev_node.next = n1_curr_node
    
    def swap_nodes(self, key_1, key_2): # Another way to Swap Nodes

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    def reverse_iterative(self):
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next   #storing the next element
            cur.next = prev  #reversing the pointer --making curr next element previous one
            prev = cur       #moving the prev to curret node
            cur = nxt        #moving the curr node to next
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None) 

    #Merge Two Sorted Linked Lists
    def merge(self,ll2):
        p = self.head
        s = None
        q = ll2.head
        count = 0
        while p and q :
            if p.data >= q.data:
                s.next = q
                s = q
                q = s.next          
            else:
                if count >1: 
                    s.next = p
                s = p
                p = s.next
            if count == 0:
                merge_llist_head = s
            count +=1
        if not p:
            s.next = q 
        if not q:
            s.next = p
        self.head = merge_llist_head
        
        
          
    
    
    
    def merge_sorted(self, llist):  # A simple Vanilla way to merge sorted list
        p = self.head 
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p

        self.head = new_head     
        return self.head

    def remove_duplicates(self):
        dup_values = {}
        cur_node = self.head
        prev_node = None
        while cur_node:
            if cur_node.data in dup_values:
                prev_node.next = cur_node.next
                cur_node = None
            else:
                dup_values[cur_node.data] = 1
                prev_node = cur_node
            cur_node = prev_node.next

    def nth_to_last_node(self,n):
        if n > self.length():
            return
        cur_node = self.head
        prev_node = None
        index = 0 
        while cur_node:
            if index == n:
                self.head = cur_node
                self.printl()
            index += 1
            cur_node = cur_node.next
    
    def print_nth_from_last(self, n):
        total_len = self.len_iterative()
        
        cur = self.head 
        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return  

    def print_nth_from_last(self, n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.next
                
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None

    def count_occurence_iterative(self,element):
        cur = self.head
        prev = None
        count = 0
        while cur:
            if cur.data == element:
                count+=1
            cur = cur.next
        return count

    def count_occurence_recursive(self, node, element):
        if not node:
            return 0
       
        if node.data == element:
            return 1+ self.count_occurence_recursive(node.next,element)
        else:
            return self.count_occurence_recursive(node.next,element)
    
    def rotate(self,element):
        # head = self.head
        cur = self.head
        while cur:
            if cur.data == element:
                pivot = cur
            if cur.next == None:
                last_node = cur
            cur = cur.next
        last_node.next = self.head 
        self.head = pivot.next
        pivot.next = None

    def rotate(self, k):            #another way to rotate the linked list
        if self.head and self.head.next:
            p = self.head 
            q = self.head 
            prev = None
            count = 0
            
            while p and count < k:
                prev = p
                p = p.next 
                q = q.next 
                count += 1
            p = prev
            while q:
                prev = q 
                q = q.next 
            q = prev 

            q.next = self.head 
            self.head = p.next 
            p.next = None
    
    def is_palindrome(self,mtd): 
        if mtd ==1:  #using a string
            s = ''
            p = self.head
            while p:
                s += p.data
                p = p.next
            return s == s[::-1]
        if mtd ==2:  #using a stack
            p = self.head
            s = []
            while p:
                s.append(p)
                p = p.next
            p = self.head
            while p:
                data = s.pop()
                if p.data != data:
                    return False
                p = p.next
            return True
        
        if mtd == 3: #using two pointers
            if self.head:
                p = self.head
                self.reverse_iterative()
                q = self.head
                while p:
                    if p.data != q.data:
                        return False
                    p = p.next
                    q = q.next
                return True
    
    def move_tail_to_head(self):
        p = self.head
        head = self.head
        switch = 0
        while p:
            tail = p
            if switch == 0:
                if p.next.next == None:
                    tail_prev = p
                    switch = 1
            p = p.next
        
        tail.next = head
        self.head = tail
        tail_prev.next = None

    def move_tail_to_head_improved(self):
        p = self.head
        head = self.head
        switch = 0
        while p.next:
            tail = p.next
            tail_prev = p 
            p = p.next
        tail.next = head
        self.head = tail
        tail_prev.next = None
    
    def move_tail_to_head_2(self): 
        if self.head and self.head.next:
            last = self.head 
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head 
            second_to_last.next = None 
            self.head = last
        
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        num1 = ''
        num2 = ''

        while p:
            num1+=str(p.data)
            p = p.next
        
        while q:
            num2+=str(q.data)
            q = q.next
        
        num = int(num1) + int(num2)

        result_ll = LinkedList()
        for i in range(len(str(num))):
            result_ll.append(str(num)[i])
        
        return result_ll
    
    def sum_two_lists(self, llist): #with less time complexity
        p = self.head  
        q = llist.head

        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0 
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist
        

        


            
            




# if "__name__" == "__main__":
llist_1 = LinkedList()
llist_2 = LinkedList()
llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(4)
llist_1.append(0)
# llist.node_swap("4","5")
# llist.swap_nodes("4","5")
# llist.del_at_index(4)
# print(llist.len_recursive(llist.head))
# llist.del_value("6")
# llist.index(-4)
llist_2.append(2)
llist_2.append(3)
llist_2.append(5)
llist_2.append(5)
llist_2.append(5)
# llist_1.merge(llist_2)
# print(llist_1.reverse_recursive())
# llist_1.remove_duplicates()
# print(llist_1.print_nth_from_last(5))
# print(llist_1.count_occurence_recursive(llist_1.head,5))
# llist_1.rotate(7)
# print(llist_1.is_palindrome(3))
# llist_1.move_tail_to_head_improved()
llist_1.sum_two_lists(llist_2).printl()
# llist_1.printl() # orignal llist 3 4 9 5 6


