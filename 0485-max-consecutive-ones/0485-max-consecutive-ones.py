class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ky_luc = 0
        dem_hien_tai = 0
        
        for so in nums:
            if so == 1:
                dem_hien_tai += 1
                # Nếu số lần đếm hiện tại vượt qua kỷ lục cũ thì cập nhật kỷ lục mới
                if dem_hien_tai > ky_luc:
                    ky_luc = dem_hien_tai
            else:
                # Gặp số 0 thì reset bộ đếm về 0
                dem_hien_tai = 0 
                
        return ky_luc