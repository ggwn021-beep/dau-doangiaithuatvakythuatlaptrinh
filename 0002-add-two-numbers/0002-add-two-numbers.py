class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Node ảo để dễ dàng nối các node kết quả vào sau
        node_ao = ListNode(0)
        hien_tai = node_ao
        nho_so = 0 # Biến "nhớ" (carry)
        
        # Lặp khi l1 còn, hoặc l2 còn, hoặc vẫn còn số nhớ (vd: 5+5=10 phải nhớ 1 văng ra ngoài)
        while l1 is not None or l2 is not None or nho_so > 0:
            gia_tri_1 = l1.val if l1 else 0
            gia_tri_2 = l2.val if l2 else 0
            
            # Thực hiện phép cộng
            tong = gia_tri_1 + gia_tri_2 + nho_so
            
            # Tính phần dư (ghi xuống) và phần nhớ (đẩy sang cột tiếp)
            ghi_xuong = tong % 10
            nho_so = tong // 10
            
            # Tạo node mới và nối vào chuỗi kết quả
            hien_tai.next = ListNode(ghi_xuong)
            hien_tai = hien_tai.next
            
            # Nhích l1 và l2 lên cột tiếp theo
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # Bỏ đi node ảo ở đầu
        return node_ao.next