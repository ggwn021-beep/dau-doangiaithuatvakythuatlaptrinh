class Solution(object):
    def findContentChildren(self, g, s):
        # Sắp xếp lại child (g) và cookies (s) từ nhỏ đến lớn
        g.sort()
        s.sort()
        
        child = 0  # Ngón tay chỉ vào em bé hiện tại
        cookies = 0   # Ngón tay chỉ vào cái bánh hiện tại
        
        # Duyệt khi vẫn còn em bé chưa có bánh VÀ vẫn còn bánh trong rổ
        while child < len(g) and cookies < len(s):
            if s[cookies] >= g[child]:
                # Em bé chịu ăn bánh
                child += 1  # Chuyển sang bé tiếp theo
            
            # Dù em bé có chịu ăn hay không, cái bánh này cũng đã được xét xong
            # (Hoặc bị ăn mất, hoặc bị chê vứt đi), nên ta phải xét cái bánh tiếp theo
            cookies += 1
            
        # Vị trí của bé hiện tại chính là tổng số em bé đã được ăn bánh
        return child