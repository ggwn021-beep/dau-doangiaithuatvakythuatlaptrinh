class Solution(object):
    def isSubsequence(self, s, t):
        # Hai ngón tay trỏ vào vị trí bắt đầu của s và t
        i = 0
        j = 0
        
        # Cứ đi tìm cho đến khi hết chữ ở s, hoặc đi hết hành lang t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Tìm thấy chữ cái hiện tại rồi, chuyển sang tìm chữ tiếp theo của s
            j += 1      # Ngón tay ở t luôn luôn tiến lên phía trước
            
        # Nếu ngón tay i đi được đến cuối chữ s là đã tìm thấy hết
        return i == len(s)