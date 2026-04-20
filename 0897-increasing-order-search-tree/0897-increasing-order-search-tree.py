class Solution(object):
    def increasingBST(self, root):
        node_ao = TreeNode(0)
        self.hien_tai = node_ao # Con trỏ dùng để nối các node lại với nhau
        
        def duyet_inorder(node):
            if not node:
                return
                
            # 1. Đi sang tận cùng bên TRÁI
            duyet_inorder(node.left)
            
            # 2. Xử lý GỐC (Thay đổi dây nối)
            node.left = None # Chặt đứt nhánh trái của node này
            self.hien_tai.right = node # Gắn node này vào bên phải của dây chuyền
            self.hien_tai = node # Nhích con trỏ tiến lên 1 bước
            
            # 3. Đi sang PHẢI
            duyet_inorder(node.right)
            
        duyet_inorder(root)
        return node_ao.right