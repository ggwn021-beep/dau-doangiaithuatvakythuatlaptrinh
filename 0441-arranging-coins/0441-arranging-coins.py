class Solution(object):
    def arrangeCoins(self, n):
        trai = 1
        phai = n
        
        while trai <= phai:
            k = trai + (phai - trai) // 2
            
            # Tính tổng số xu cần thiết để xếp được k hàng
            tong_xu_can = k * (k + 1) // 2
            
            if tong_xu_can == n:
                return k # Vừa khít số xu
            elif tong_xu_can > n:
                phai = k - 1 # Không đủ xu, phải giảm số hàng xuống
            else:
                trai = k + 1 # Vẫn còn dư xu, thử tăng số hàng lên
                
        # Trả về 'phai' vì ta cần số hàng hoàn chỉnh lớn nhất không vượt quá n
        return phai