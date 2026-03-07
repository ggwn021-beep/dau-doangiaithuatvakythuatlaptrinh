class Solution(object):
    def strStr(self, haystack, needle):
        do_dai_h = len(haystack)
        do_dai_n = len(needle)
        
        # Nếu n dài hơn cả h thì vô lý, không thể tìm thấy
        if do_dai_n > do_dai_h:
            return -1
            
        # Trượt cái khung từ đầu đến cuối đống rơm
        for i in range(do_dai_h - do_dai_n + 1):
            # Cắt một đoạn h bằng với kích thước n để so sánh
            if haystack[i : i + do_dai_n] == needle:
                return i # Trả về vị trí bắt đầu của khung
                
        return -1