class Solution(object):
    def reverseString(self, s):
        trai = 0
        phai = len(s) - 1
        
        while trai < phai:
            # Hoán đổi giá trị của 2 ô nhớ
            s[trai], s[phai] = s[phai], s[trai]
            
            # Tiến dần vào giữa
            trai += 1
            phai -= 1