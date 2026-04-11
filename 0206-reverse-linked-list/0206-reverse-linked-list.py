# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        truoc = None # Ban đầu chưa có ai ở đằng trước
        hien_tai = head
        
        while hien_tai is not None:
            # 1. Giữ lấy bạn đằng sau- nếu không buông tay ra sẽ bị lạc mất
            sau = hien_tai.next 
            
            # 2. Hành động chính: Quay ngược lại nắm tay bạn đằng trước
            hien_tai.next = truoc 
            
            # 3. Hai bạn rủ nhau cùng tiến lên 1 bước để xử lý người tiếp theo
            truoc = hien_tai
            hien_tai = sau
            
        # Cuối cùng, người cuối cùng (giờ là 'truoc') sẽ trở thành đầu hàng mới
        return truoc