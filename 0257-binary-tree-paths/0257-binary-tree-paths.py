class Solution(object):
    def binaryTreePaths(self, root):
        ket_qua = []
        
        def tim_duong(node, duong_di_hien_tai):
            if not node:
                return
                
            # Ghi nhận trạm hiện tại vào đường đi
            duong_di_hien_tai += str(node.val)
            
            # Nếu đây là ngõ cụt (Node lá) -> Chụp ảnh nộp về tổng đài
            if not node.left and not node.right:
                ket_qua.append(duong_di_hien_tai)
                return
                
            # Nếu chưa phải ngõ cụt, đi tiếp và thêm mũi tên
            duong_di_hien_tai += "->"
            tim_duong(node.left, duong_di_hien_tai)
            tim_duong(node.right, duong_di_hien_tai)
            
        tim_duong(root, "")
        return ket_qua