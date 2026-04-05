class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ket_qua = []
        n = len(nums)
        
        for i in range(n - 3):
            # Khử nếu trùng bạn A
            if i > 0 and nums[i] == nums[i - 1]: continue
                
            for j in range(i + 1, n - 2):
                # Khử nếu trùng bạn B
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                    
                trai = j + 1
                phai = n - 1
                
                while trai < phai:
                    tong = nums[i] + nums[j] + nums[trai] + nums[phai]
                    
                    if tong == target:
                        ket_qua.append([nums[i], nums[j], nums[trai], nums[phai]])
                        # Khử nếu trùng 2 bạn kẹp giữa
                        while trai < phai and nums[trai] == nums[trai + 1]: trai += 1
                        while trai < phai and nums[phai] == nums[phai - 1]: phai -= 1
                        trai += 1
                        phai -= 1
                    elif tong < target:
                        trai += 1
                    else:
                        phai -= 1
                        
        return ket_qua