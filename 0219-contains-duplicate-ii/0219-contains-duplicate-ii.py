class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        so_tay_vi_tri = {}
        
        for i, so in enumerate(nums):
            # Nếu số này đã từng xuất hiện VÀ khoảng cách <= k
            if so in so_tay_vi_tri and i - so_tay_vi_tri[so] <= k:
                return True
                
            # Ghi đè vị trí mới nhất của con số này vào sổ
            so_tay_vi_tri[so] = i
            
        return False