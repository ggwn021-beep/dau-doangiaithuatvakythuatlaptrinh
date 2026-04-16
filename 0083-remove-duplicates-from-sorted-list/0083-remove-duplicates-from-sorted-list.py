class Solution(object):
    def deleteDuplicates(self, head):
        hien_tai = head
        
        while hien_tai and hien_tai.next:
            # Nếu phát hiện người đằng sau giống hệt mình
            if hien_tai.val == hien_tai.next.val:
                # Bắc cầu vượt mặt người đó (vứt người đó đi)
                hien_tai.next = hien_tai.next.next
            else:
                # Nếu khác nhau thì an toàn tiến lên 1 bước
                hien_tai = hien_tai.next
                
        return head