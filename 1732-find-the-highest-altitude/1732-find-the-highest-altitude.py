class Solution(object):
    def largestAltitude(self, gain):
        max_alt = 0      # Lưu kỷ lục cao nhất
        current_alt = 0  # Lưu trạng thái độ cao hiện tại
        
        for g in gain:
            current_alt += g  # Cập nhật độ cao
            # Hàm max() so sánh kỷ lục cũ và độ cao mới
            if current_alt > max_alt:
                max_alt = current_alt
                
        return max_alt