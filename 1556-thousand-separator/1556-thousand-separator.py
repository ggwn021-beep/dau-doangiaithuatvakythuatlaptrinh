class Solution(object):
    def thousandSeparator(self, n):
        chuoi_so = str(n)
        if len(chuoi_so) <= 3:
            return chuoi_so
            
        ket_qua = ""
        dem = 0
        
        # Đi ngược từ cuối (hàng đơn vị) lên đầu
        for i in range(len(chuoi_so) - 1, -1, -1):
            ket_qua = chuoi_so[i] + ket_qua
            dem += 1
            
            # Cứ đếm đủ 3 số, và chưa phải là số tận cùng ở đầu thì chấm 1 cái
            if dem == 3 and i != 0:
                ket_qua = "." + ket_qua
                dem = 0 # Đếm lại từ đầu
                
        return ket_qua