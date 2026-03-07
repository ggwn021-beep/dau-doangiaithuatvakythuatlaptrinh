class Solution(object):
    def pivotIndex(self, nums):
        tong_tat_ca = sum(nums)
        tong_trai = 0
        
        for i in range(len(nums)):
            # Tính tổng phần còn lại bên phải
            tong_phai = tong_tat_ca - tong_trai - nums[i]
            
            # Cân bằng thì dừng lại báo cáo vị trí
            if tong_trai == tong_phai:
                return i 
                
            # Nếu chưa cân bằng, nhét người này sang nhóm bên Trái để xét vị trí tiếp theo
            tong_trai += nums[i]
            
        return -1