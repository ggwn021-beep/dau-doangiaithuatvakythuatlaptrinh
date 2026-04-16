class Solution(object):
    def hasPathSum(self, root, targetSum):
        # Nếu đi vào ngõ cụt mà không phải Node lá, hoặc cây rỗng
        if not root:
            return False
            
        # Trừ số tiền nhặt được ở Node hiện tại
        so_tien_con_thieu = targetSum - root.val
        
        # Nếu đã chạm đất (Node lá) VÀ số tiền còn thiếu vừa đủ bằng 0
        if not root.left and not root.right:
            return so_tien_con_thieu == 0
            
        # Chia nhau ra đi tìm ở nhánh trái hoặc nhánh phải (chỉ cần 1 bên đúng là được)
        nhanh_trai_dung = self.hasPathSum(root.left, so_tien_con_thieu)
        nhanh_phai_dung = self.hasPathSum(root.right, so_tien_con_thieu)
        
        return nhanh_trai_dung or nhanh_phai_dung