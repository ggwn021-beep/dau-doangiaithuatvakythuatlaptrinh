class Solution(object):
    def mostWordsFound(self, sentences):
        ky_luc = 0
        
        for cau in sentences:
            # Số từ = Số khoảng trắng + 1
            so_tu = cau.count(" ") + 1
            if so_tu > ky_luc:
                ky_luc = so_tu
                
        return ky_luc