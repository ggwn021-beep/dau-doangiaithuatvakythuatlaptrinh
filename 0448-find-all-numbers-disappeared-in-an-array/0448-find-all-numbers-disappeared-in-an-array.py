class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Bước 1: Điểm danh và đánh dấu
        for i in range(len(nums)):
            # Lấy giá trị tuyệt đối vì số này có thể đã bị "bôi đen" (thành số âm) trước đó
            so_hien_tai = abs(nums[i])
            vi_tri_ghe = so_hien_tai - 1
            
            # Đánh dấu người này đã đi học bằng cách biến số tại ghế đó thành số âm
            if nums[vi_tri_ghe] > 0:
                nums[vi_tri_ghe] *= -1
                
        # Bước 2: Kt xem ghế nào chưa bị đánh dấu (vẫn là số dương)
        danh_sach_vang = []
        for i in range(len(nums)):
            if nums[i] > 0:
                danh_sach_vang.append(i + 1)
                
        return danh_sach_vang