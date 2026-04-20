from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
            
        ket_qua = []
        # Khởi tạo hàng đợi với phần tử đầu tiên là Gốc
        hang_doi = deque([root])
        
        while hang_doi:
            so_luong_node_tang_nay = len(hang_doi)
            tang_hien_tai = []
            
            # Chỉ lấy ĐÚNG số lượng Node của tầng này ra xử lý
            for _ in range(so_luong_node_tang_nay):
                node = hang_doi.popleft()
                tang_hien_tai.append(node.val)
                
                # Sau khi lấy ra, đẩy các con của nó (thuộc tầng tiếp theo) vào chờ
                if node.left: hang_doi.append(node.left)
                if node.right: hang_doi.append(node.right)
                
            ket_qua.append(tang_hien_tai)
            
        return ket_qua