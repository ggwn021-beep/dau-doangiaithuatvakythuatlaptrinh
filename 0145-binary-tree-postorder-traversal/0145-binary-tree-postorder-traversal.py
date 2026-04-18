class Solution(object):
    def postorderTraversal(self, root):
        ket_qua = []
        
        def duyet_cay(node):
            if not node:
                return
            
            # 1. Dọn sạch cành TRÁI
            duyet_cay(node.left)
            # 2. Dọn sạch cành PHẢI
            duyet_cay(node.right)
            # 3. Cuối cùng mới xử lý GỐC (Giữa)
            ket_qua.append(node.val)
            
        duyet_cay(root)
        return ket_qua