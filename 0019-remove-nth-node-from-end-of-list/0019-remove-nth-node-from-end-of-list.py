class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Node ảo dùng để đỡ trường hợp danh sách chỉ có 1 Node hoặc xóa đúng Node đầu tiên
        node_ao = ListNode(0, head)
        cham = node_ao
        nhanh = node_ao
        
        # Cho ban Trinh Sát (nhanh) đi trước n bước
        for _ in range(n):
            nhanh = nhanh.next
            
        # Cho cả 2 cùng tiến lên đến khi ban Trinh Sát chạm đáy
        while nhanh.next:
            cham = cham.next
            nhanh = nhanh.next
            
        # Cắt bỏ Node bằng cách bắc cầu vượt qua nó
        cham.next = cham.next.next
        
        return node_ao.next