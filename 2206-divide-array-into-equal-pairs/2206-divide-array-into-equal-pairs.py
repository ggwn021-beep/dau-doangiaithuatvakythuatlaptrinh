import collections

class Solution(object):
    def divideArray(self, nums):
        # Hệ điều hành gọi C-backend để đếm tần suất siêu nhanh
        so_tay_dem = collections.Counter(nums)
        
        for so_luong in so_tay_dem.values():
            # Nếu có bất kỳ con số nào xuất hiện với số lần LẺ -> Không thể chia cặp
            if so_luong % 2 != 0:
                return False
                
        return True