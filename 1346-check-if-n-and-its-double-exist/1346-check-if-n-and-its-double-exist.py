class Solution(object):
    def checkIfExist(self, arr):
        so_tay = set()
        
        for so in arr:
            # Kiểm tra xem số gấp đôi hoặc số bằng một nửa (nếu là số chẵn) có trong sổ chưa
            if (so * 2 in so_tay) or (so % 2 == 0 and so // 2 in so_tay):
                return True
                
            # Nếu chưa có, ghi số này vào sổ tay để các số sau tra cứu
            so_tay.add(so)
            
        return False