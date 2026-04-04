class Solution(object):
    def findClosestNumber(self, nums):
        so_gan_nhat = nums[0]
        
        for so in nums:
            # So sánh khoảng cách (dùng trị tuyệt đối abs)
            khoang_cach_hien_tai = abs(so)
            khoang_cach_ky_luc = abs(so_gan_nhat)
            
            if khoang_cach_hien_tai < khoang_cach_ky_luc:
                so_gan_nhat = so
            # Nếu khoảng cách bằng nhau, ưu tiên lấy số lớn hơn (ví dụ ưu tiên 2 thay vì -2)
            elif khoang_cach_hien_tai == khoang_cach_ky_luc:
                so_gan_nhat = max(so_gan_nhat, so)
                
        return so_gan_nhat