class Solution(object):
    def maxProfit(self, prices):
        gia_re_nhat = float('inf') # Khởi tạo bằng vô cực
        loi_nhuan_ky_luc = 0
        
        for gia_hom_nay in prices:
            # 1. Cập nhật giá rẻ nhất nếu thấy
            if gia_hom_nay < gia_re_nhat:
                gia_re_nhat = gia_hom_nay
                
            # 2. Tính thử lợi nhuận nếu bán hôm nay
            loi_nhuan_thu_nghiem = gia_hom_nay - gia_re_nhat
            
            # 3. Xem có phá kỷ lục không
            if loi_nhuan_thu_nghiem > loi_nhuan_ky_luc:
                loi_nhuan_ky_luc = loi_nhuan_thu_nghiem
                
        return loi_nhuan_ky_luc