class Solution(object):
    def isValidBST(self, root):
        
        def kiem_tra(node, gioi_han_duoi, gioi_han_tren):
            # Nếu chạm đáy -> Vùng này hợp lệ
            if not node:
                return True
                
            # Nếu người này vi phạm ranh giới (Quá nhỏ hoặc Quá lớn) -> Loai
            if node.val <= gioi_han_duoi or node.val >= gioi_han_tren:
                return False
                
            # Kiểm tra nhánh bên trái (Max của nó giờ là chính nó)
            ben_trai_ok = kiem_tra(node.left, gioi_han_duoi, node.val)
            # Kiểm tra nhánh bên phải (Min của nó giờ là chính nó)
            ben_phai_ok = kiem_tra(node.right, node.val, gioi_han_tren)
            
            return ben_trai_ok and ben_phai_ok
            
        # Khởi đầu biên độ là vô cực
        return kiem_tra(root, float('-inf'), float('inf'))