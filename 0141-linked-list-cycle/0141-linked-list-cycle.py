class Solution(object):
    def hasCycle(self, head):
        rua = head
        tho = head
        
        # Thỏ chạy nhanh nên phải kiểm tra xem Thỏ có đụng ngõ cụt chưa
        while tho and tho.next:
            rua = rua.next           # Rùa đi 1 bước
            tho = tho.next.next      # Thỏ nhảy 2 bước
            
            if rua == tho:           # Đụng nhau thi co vong lap
                return True
                
        return False # Thỏ chạy tới đích bình yên, không có vòng lặp