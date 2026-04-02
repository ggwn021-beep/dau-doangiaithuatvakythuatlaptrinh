class Solution(object):
    def findFinalValue(self, nums, original):
        # Biến danh sách thành Bảng băm (Set) để tìm kiếm tức thì O(1)
        tap_hop_so = set(nums)
        
        # Chừng nào con số này vẫn còn nằm trong Bảng băm thì cứ nhân đôi
        while original in tap_hop_so:
            original = original * 2
            
        return original