class Solution(object):
    def lemonadeChange(self, bills):
        # Két sắt của bạn
        to_5 = 0
        to_10 = 0
        
        for tien_khach_dua in bills:
            if tien_khach_dua == 5:
                to_5 += 1
            elif tien_khach_dua == 10:
                if to_5 == 0:
                    return False # Không có tiền thối
                to_5 -= 1
                to_10 += 1
            else: # Khách đưa 20
                # Tham lam: Ưu tiên thối tờ $10 trước và giữ lại tờ $5
                if to_10 > 0 and to_5 > 0:
                    to_10 -= 1
                    to_5 -= 1
                # Nếu không có tờ $10 thì mới dùng 3 tờ $5
                elif to_5 >= 3:
                    to_5 -= 3
                else:
                    return False # Toang
                    
        return True