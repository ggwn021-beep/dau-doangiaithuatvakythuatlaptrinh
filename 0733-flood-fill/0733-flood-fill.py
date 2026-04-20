class Solution(object):
    def floodFill(self, image, sr, sc, color):
        mau_cu = image[sr][sc]
        
        # Ngăn chặn vòng lặp vô tận nếu màu mới và màu cũ giống hệt nhau
        if mau_cu == color:
            return image
            
        hang = len(image)
        cot = len(image[0])
        
        def to_mau(r, c):
            # Nếu chạy ra ngoài bức ảnh, HOẶC gặp ô không phải màu cũ -> Dừng loang
            if r < 0 or r >= hang or c < 0 or c >= cot or image[r][c] != mau_cu:
                return
                
            # Tô màu mới cho ô hiện tại
            image[r][c] = color
            
            # Loang mực ra 4 hướng
            to_mau(r - 1, c) # Lên
            to_mau(r + 1, c) # Xuống
            to_mau(r, c - 1) # Trái
            to_mau(r, c + 1) # Phải
            
        to_mau(sr, sc)
        return image