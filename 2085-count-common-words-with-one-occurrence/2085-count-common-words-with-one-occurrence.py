import collections

class Solution(object):
    def countWords(self, words1, words2):
        # Hệ điều hành gọi hàm C cấp thấp để băm (Hash) và đếm cực nhanh
        dem_1 = collections.Counter(words1)
        dem_2 = collections.Counter(words2)
        
        ket_qua = 0
        
        for tu, so_lan in dem_1.items():
            # Điều kiện AND: Bên mảng 1 xuất hiện 1 lần VÀ bên mảng 2 cũng có + xuất hiện 1 lần
            if so_lan == 1 and dem_2.get(tu, 0) == 1:
                ket_qua += 1
                
        return ket_qua