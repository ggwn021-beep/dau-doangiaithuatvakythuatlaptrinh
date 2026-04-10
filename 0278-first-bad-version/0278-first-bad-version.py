# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        trai = 1
        phai = n
        
        while trai < phai:
            giua = trai + (phai - trai) // 2
            
            # Nếu phiên bản giữa BỊ LỖI
            if isBadVersion(giua):
                # Phiên bản lỗi đầu tiên có thể là 'giua' hoặc nằm trước 'giua'
                phai = giua 
            else:
                # Nếu không lỗi, chắc chắn vùng lỗi nằm sau 'giua'
                trai = giua + 1
                
        # Khi trai đụng phai, đó chính là phiên bản lỗi đầu tiên
        return trai