from collections import deque

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
            
        # Hàng đợi lưu trữ: (Node hiện tại, Độ sâu của node đó)
        hang_doi = deque([(root, 1)])
        
        while hang_doi:
            node_hien_tai, do_sau = hang_doi.popleft()
            
            # Nếu là Node lá (không có con trái & phải) -> Chắc chắn là ngắn nhất!
            if not node_hien_tai.left and not node_hien_tai.right:
                return do_sau
                
            # Đẩy các con ở tầng tiếp theo vào hàng đợi
            if node_hien_tai.left:
                hang_doi.append((node_hien_tai.left, do_sau + 1))
            if node_hien_tai.right:
                hang_doi.append((node_hien_tai.right, do_sau + 1))