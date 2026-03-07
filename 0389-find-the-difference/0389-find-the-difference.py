class Solution(object):
    def findTheDifference(self, s, t):
        tong_can_nang_s = 0
        tong_can_nang_t = 0
        
        # Đem S lên cân
        for chu in s:
            tong_can_nang_s += ord(chu) # ord() là hàm lấy trọng lượng (mã ASCII)
            
        # Đem T lên cân
        for chu in t:
            tong_can_nang_t += ord(chu)
            
        # Hiệu số cân nặng chính là mã ASCII của chữ cái bị thừa
        chu_cai_thua = tong_can_nang_t - tong_can_nang_s
        
        return chr(chu_cai_thua) # chr() là hàm biến trọng lượng thành lại chữ cái