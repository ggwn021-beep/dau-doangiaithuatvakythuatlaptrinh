class Solution(object):
    def prefixCount(self, words, pref):
        dem = 0
        
        for tu in words:
            # Dùng hàm hệ thống startswith để tối ưu thao tác trên RAM
            if tu.startswith(pref):
                dem += 1
                
        return dem