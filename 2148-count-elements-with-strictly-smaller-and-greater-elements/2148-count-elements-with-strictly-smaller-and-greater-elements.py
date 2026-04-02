class Solution(object):
    def countElements(self, nums):
        # Tìm giá trị Nhỏ nhất và Lớn nhất bằng hàm tích hợp
        nho_nhat = min(nums)
        lon_nhat = max(nums)
        
        dem = 0
        # Quét mảng để tìm những kẻ "lưng chừng"
        for so in nums:
            if nho_nhat < so < lon_nhat:
                dem += 1
                
        return dem