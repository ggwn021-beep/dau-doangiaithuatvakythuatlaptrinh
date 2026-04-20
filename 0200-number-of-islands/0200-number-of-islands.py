class Solution(object):
    def numIslands(self, grid):
        if not grid: return 0
        
        so_dao = 0
        hang = len(grid)
        cot = len(grid[0])
        
        # Hàm đệ quy để đánh chìm-đổi 1 thành 0-toàn bộ hòn đảo
        def danh_chim(r, c):
            # Nếu đi ra ngoài bản đồ, hoặc gặp nước ('0') -> Dừng lại
            if r < 0 or r >= hang or c < 0 or c >= cot or grid[r][c] == '0':
                return
                
            # Đổi đất thành nước
            grid[r][c] = '0'
            
            # Lan ra 4 hướng: Trên, Dưới, Trái, Phải
            danh_chim(r - 1, c)
            danh_chim(r + 1, c)
            danh_chim(r, c - 1)
            danh_chim(r, c + 1)
            
        # Dùng thuyền đi dò từng ô trên bản đồ
        for r in range(hang):
            for c in range(cot):
                # Nếu phát hiện Đất
                if grid[r][c] == '1':
                    so_dao += 1 # Đếm được 1 đảo
                    danh_chim(r, c) # Lập tức đánh chìm toàn bộ phần đất nối liền với nó
                    
        return so_dao