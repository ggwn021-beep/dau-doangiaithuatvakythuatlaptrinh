class Solution(object):
    def searchBST(self, root, val):
        hien_tai = root
        
        while hien_tai is not None:
            if hien_tai.val == val:
                return hien_tai # Dúng roi
            elif val < hien_tai.val:
                # Giá trị cần tìm nhỏ hơn -> Rẽ Trái
                hien_tai = hien_tai.left
            else:
                # Giá trị cần tìm lớn hơn -> Rẽ Phải
                hien_tai = hien_tai.right
                
        # Đi đến ngõ cụt mà vẫn không thấy
        return None