class Solution(object):
    def heightChecker(self, heights):
        # Tạo đội hình mẫu bằng cách sắp xếp hàng thật
        doi_hinh_mau = sorted(heights)
        so_ban_sai_vi_tri = 0
        
        # Đi dọc theo 2 hàng để so sánh từng cặp
        for i in range(len(heights)):
            if heights[i] != doi_hinh_mau[i]:
                so_ban_sai_vi_tri += 1
                
        return so_ban_sai_vi_tri