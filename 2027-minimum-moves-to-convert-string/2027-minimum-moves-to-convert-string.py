class Solution(object):
    def minimumMoves(self, s):
        so_buoc = 0
        i = 0
        
        while i < len(s):
            # Nếu phát hiện vết bẩn 'X'
            if s[i] == 'X':
                so_buoc += 1
                # Vung cọ sơn đè lên 3 ô, nên ta nhảy cóc qua 3 ô đó luôn
                i += 3
            else:
                # Nếu đã sạch ('O'), đi bộ sang ô tiếp theo
                i += 1
                
        return so_buoc