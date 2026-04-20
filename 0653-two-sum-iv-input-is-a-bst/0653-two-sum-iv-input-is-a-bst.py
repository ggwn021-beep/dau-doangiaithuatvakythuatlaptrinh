class Solution(object):
    def findTarget(self, root, k):
        so_tay = set()
        
        def duyet_cay(node):
            if not node:
                return False
                
            so_con_thieu = k - node.val
            
            # Nếu số còn thiếu ĐÃ TỒN TẠI trong sổ tay -> Thành công
            if so_con_thieu in so_tay:
                return True
                
            # Nếu chưa có, ghi số hiện tại vào sổ
            so_tay.add(node.val)
            
            # Chia ra đi tìm ở 2 nhánh, chỉ cần 1 nhánh True là được
            return duyet_cay(node.left) or duyet_cay(node.right)
            
        return duyet_cay(root)