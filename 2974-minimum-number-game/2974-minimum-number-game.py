class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        
        # Nhảy 2 bước mỗi lần vì ta xử lý theo từng đôi một
        for i in range(0, len(nums), 2):
            # Cú pháp hoán đổi 2 biến siêu nhanh của Python
            nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums