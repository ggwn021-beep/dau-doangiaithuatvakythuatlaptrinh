class Solution(object):
    def maxArea(self, height):
        trai = 0
        phai = len(height) - 1
        ky_luc_nuoc = 0
        
        while trai < phai:
            # Lượng nước bị giới hạn bởi cột thấp hơn
            chieu_cao_thuc = min(height[trai], height[phai])
            chieu_rong = phai - trai
            
            the_tich = chieu_cao_thuc * chieu_rong
            ky_luc_nuoc = max(ky_luc_nuoc, the_tich)
            
            # Luôn vứt bỏ cái cột lùn hơn để đi tìm cơ hội mới
            if height[trai] < height[phai]:
                trai += 1
            else:
                phai -= 1
                
        return ky_luc_nuoc