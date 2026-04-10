class Solution(object):
    def searchInsert(self, nums, target):
        trai = 0
        phai = len(nums) - 1
        
        while trai <= phai:
            giua = trai + (phai - trai) // 2
            
            if nums[giua] == target:
                return giua
            elif nums[giua] < target:
                trai = giua + 1
            else:
                phai = giua - 1
                
        # Nếu không tìm thấy, con trỏ 'trai' chính là vị trí cần chèn
        return trai