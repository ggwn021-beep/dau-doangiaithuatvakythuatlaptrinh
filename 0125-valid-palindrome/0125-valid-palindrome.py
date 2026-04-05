class Solution(object):
    def isPalindrome(self, s):
        trai = 0
        phai = len(s) - 1
        
        while trai < phai:
            # Hàm isalnum() kiểm tra xem có phải chữ cái hoặc số không
            # Nếu gặp rác (dấu câu, khoảng trắng) thì bỏ qua
            if not s[trai].isalnum():
                trai += 1
                continue
            if not s[phai].isalnum():
                phai -= 1
                continue
                
            # Đưa về chữ thường để so sánh bất chấp Hoa/Thường
            if s[trai].lower() != s[phai].lower():
                return False
                
            trai += 1
            phai -= 1
            
        return True