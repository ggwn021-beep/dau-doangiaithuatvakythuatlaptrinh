class Solution(object):
    def moveZeroes(self, nums):
        cham = 0 # Trỏ vào vị trí trống an toàn
        
        for nhanh in range(len(nums)):
            # Nếu gặp số khác 0, hoán đổi nó lên vị trí 'cham'
            if nums[nhanh] != 0:
                nums[cham], nums[nhanh] = nums[nhanh], nums[cham]
                cham += 1