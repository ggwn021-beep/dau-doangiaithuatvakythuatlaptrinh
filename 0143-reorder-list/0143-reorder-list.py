class Solution(object):
    def reorderList(self, head):
        if not head or not head.next: return
        
        # 1. Tìm khúc giữa (Dùng Rùa và Thỏ)
        rua, tho = head, head
        while tho and tho.next:
            rua = rua.next
            tho = tho.next.next
            
        # 2. Cắt đôi và lật ngược nửa sau
        truoc, hien_tai = None, rua.next
        rua.next = None # Chặt đứt dây nối nửa đầu và nửa sau
        
        while hien_tai:
            sau = hien_tai.next
            hien_tai.next = truoc
            truoc = hien_tai
            hien_tai = sau
            
        # 3. Trộn 2 nửa lại với nhau
        nua_dau, nua_sau = head, truoc
        while nua_sau:
            # Giữ dây
            day_dau = nua_dau.next
            day_sau = nua_sau.next
            
            # Đan chéo: Node đầu chỉ vào Node cuối
            nua_dau.next = nua_sau
            # Node cuối chỉ vào Node thứ hai
            nua_sau.next = day_dau
            
            # Tiến lên bước tiếp theo
            nua_dau = day_dau
            nua_sau = day_sau