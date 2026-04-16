# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        # Cô giáo Ảo đứng trước người đầu tiên
        node_ao = ListNode(0)
        node_ao.next = head
        
        hien_tai = node_ao
        
        while hien_tai.next is not None:
            # Nếu người tiếp theo mặc áo màu 'val'
            if hien_tai.next.val == val:
                # Bắc cầu vượt qua người đó
                hien_tai.next = hien_tai.next.next
            else:
                # Nếu không phải, an toàn bước tới 1 bước
                hien_tai = hien_tai.next
                
        return node_ao.next