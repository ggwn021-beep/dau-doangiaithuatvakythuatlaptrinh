class Solution(object):
    def mergeTwoLists(self, list1, list2):
        node_ao = ListNode(0)
        hien_tai = node_ao
        
        while list1 and list2:
            if list1.val < list2.val:
                hien_tai.next = list1
                list1 = list1.next
            else:
                hien_tai.next = list2
                list2 = list2.next
            hien_tai = hien_tai.next
            
        # Nối phần đuôi còn sót lại của 1 trong 2 list
        hien_tai.next = list1 if list1 else list2
        
        return node_ao.next