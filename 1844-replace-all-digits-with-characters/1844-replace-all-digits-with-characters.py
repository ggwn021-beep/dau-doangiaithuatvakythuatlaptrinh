class Solution(object):
    def replaceDigits(self, s):
        # Biến chuỗi thành mảng (List)
        mang_ky_tu = list(s)
        
        # Chỉ duyệt qua các vị trí là Chữ số
        for i in range(1, len(mang_ky_tu), 2):
            chu_truoc_do = mang_ky_tu[i - 1]
            khoang_cach = int(mang_ky_tu[i])
            
            chu_moi = chr(ord(chu_truoc_do) + khoang_cach)
            
            mang_ky_tu[i] = chu_moi
            
        return "".join(mang_ky_tu)