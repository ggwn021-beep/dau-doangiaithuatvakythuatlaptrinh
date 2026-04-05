class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ket_qua = []
        n = len(nums)
        
        for i in range(n - 2):
            # Bỏ qua nếu Cột mốc (i) giống hệt thằng đứng trước nó
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            trai = i + 1
            phai = n - 1
            
            while trai < phai:
                tong = nums[i] + nums[trai] + nums[phai]
                
                if tong == 0:
                    # Ghi nhận kết quả
                    ket_qua.append([nums[i], nums[trai], nums[phai]])
                    
                    # Bỏ qua trùng lặp cho con trỏ trái và phải
                    while trai < phai and nums[trai] == nums[trai + 1]:
                        trai += 1
                    while trai < phai and nums[phai] == nums[phai - 1]:
                        phai -= 1
                        
                    trai += 1
                    phai -= 1
                elif tong < 0:
                    trai += 1  # Tổng nhỏ quá thì tăng thằng bên trái lên
                else:
                    phai -= 1  # Tổng to quá thì giảm thằng bên phải xuống
                    
        return ket_qua