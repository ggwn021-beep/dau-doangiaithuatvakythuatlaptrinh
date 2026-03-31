class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        xa_nhat = 0
        
        # C1: Lấy nhà đầu tiên (0) làm gốc, quét từ mép cuối đường ngược về
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                xa_nhat = max(xa_nhat, i - 0)
                break 
                
        # C2: Lấy nhà cuối cùng (n - 1) làm gốc, quét từ đầu đường xuôi tới
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                xa_nhat = max(xa_nhat, (n - 1) - i)
                break 
                
        return xa_nhat