class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        # 1. Tính tổng chuẩn mực nếu không bị thiếu số nào (Công thức Gauss)
        tong_chuan = n * (n + 1) // 2
        
        # 2. Tính tổng các số đang có thực tế
        tong_thuc_te = sum(nums)
        
        # 3. Sự chênh lệch chính là số bị thiếu
        return tong_chuan - tong_thuc_te