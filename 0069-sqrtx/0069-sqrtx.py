class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
            
        trai = 1
        phai = x // 2 # Căn bậc 2 của x (x >= 2) luôn nhỏ hơn hoặc bằng x/2
        
        while trai <= phai:
            giua = trai + (phai - trai) // 2
            binh_phuong = giua * giua
            
            if binh_phuong == x:
                return giua
            elif binh_phuong < x:
                trai = giua + 1
            else:
                phai = giua - 1
                
        # Trả về 'phai' vì đề bài yêu cầu làm tròn xuống (phần nguyên)
        return phai