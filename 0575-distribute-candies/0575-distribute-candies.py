class Solution(object):
    def distributeCandies(self, candyType):
        so_keo_duoc_an = len(candyType) // 2
        
        # Dùng set() để tự động vứt đi các viên kẹo trùng lặp, chỉ giữ lại các loại kẹo
        so_loai_keo_thuc_te = len(set(candyType))
        
        # Trả về số nhỏ hơn
        return min(so_loai_keo_thuc_te, so_keo_duoc_an)