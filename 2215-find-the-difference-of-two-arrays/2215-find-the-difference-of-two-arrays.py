class Solution(object):
    def findDifference(self, nums1, nums2):
        # Biến mảng thành Tập hợp (vừa loại bỏ trùng lặp, vừa giúp tra cứu siêu nhanh)
        tap_hop_1 = set(nums1)
        tap_hop_2 = set(nums2)
        
        # Phép trừ tập hợp: Lấy những cái có ở 1 mà không có ở 2 (và ngược lại)
        ket_qua_1 = list(tap_hop_1 - tap_hop_2)
        ket_qua_2 = list(tap_hop_2 - tap_hop_1)
        
        return [ket_qua_1, ket_qua_2]