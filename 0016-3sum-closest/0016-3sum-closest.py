class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        tong_gan_nhat = float('inf') # Khởi tạo kỷ lục là vô cực
        
        for i in range(len(nums) - 2):
            trai = i + 1
            phai = len(nums) - 1
            
            while trai < phai:
                tong = nums[i] + nums[trai] + nums[phai]
                
                # Nếu khoảng cách mới này ngắn hơn khoảng cách kỷ lục cũ -> Cập nhật
                if abs(tong - target) < abs(tong_gan_nhat - target):
                    tong_gan_nhat = tong
                    
                # Điều hướng con trỏ để ép tổng lại gần target
                if tong == target:
                    return tong # Trúng hồng tâm thì nghỉ luôn!
                elif tong < target:
                    trai += 1
                else:
                    phai -= 1
                    
        return tong_gan_nhat