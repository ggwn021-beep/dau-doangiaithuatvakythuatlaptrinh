class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
            
        tong_thoi_gian = 0
        
        # Xét khoảng thời gian giữa 2 lần bắn liên tiếp
        for i in range(len(timeSeries) - 1):
            khoang_cach_ban = timeSeries[i+1] - timeSeries[i]
            
            # Cộng khoảng thời gian nhỏ hơn giữa (khoảng cách 2 lần bắn) và (thời gian độc)
            if khoang_cach_ban < duration:
                tong_thoi_gian += khoang_cach_ban
            else:
                tong_thoi_gian += duration
                
        # Cộng thêm trọn vẹn thời gian độc của mũi tên cuối cùng (vì mũi cuối không bị ai đè lên)
        tong_thoi_gian += duration
        
        return tong_thoi_gian