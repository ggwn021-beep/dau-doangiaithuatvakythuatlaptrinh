class Solution(object):
    def countPairs(self, nums, k):
        dem = 0
        n = len(nums)
        
        # Vòng lặp lấy người thứ i
        for i in range(n):
            # Vòng lặp lấy người thứ j (luôn ngồi sau i)
            for j in range(i + 1, n):
                # Kiểm tra 2 điều kiện cốt lõi cùng lúc
                if nums[i] == nums[j] and (i * j) % k == 0:
                    dem += 1
                    
        return dem