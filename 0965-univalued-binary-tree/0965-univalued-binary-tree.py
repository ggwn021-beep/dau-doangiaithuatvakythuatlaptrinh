class Solution(object):
    def isUnivalTree(self, root):
        # Lấy giá trị của Gốc làm hệ quy chiếu
        gia_tri_chuan = root.val
        
        def kiem_tra(node):
            if not node:
                return True
                
            # Nếu phát hiện kẻ dị biệt -> Báo sai!
            if node.val != gia_tri_chuan:
                return False
                
            # Kiểm tra tiếp nhánh trái và nhánh phải
            return kiem_tra(node.left) and kiem_tra(node.right)
            
        return kiem_tra(root)