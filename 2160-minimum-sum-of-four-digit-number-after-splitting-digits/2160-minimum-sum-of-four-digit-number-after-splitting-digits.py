class Solution(object):
    def minimumSum(self, num):
        # Biến số thành danh sách các chữ số và sắp xếp tăng dần
        cac_chu_so = sorted(str(num))
        
        # Lấy 2 số nhỏ nhất (vị trí 0 và 1) làm hàng chục (nhân với 10)
        # Lấy 2 số to nhất (vị trí 2 và 3) làm hàng đơn vị
        so_thu_nhat = int(cac_chu_so[0]) * 10 + int(cac_chu_so[2])
        so_thu_hai = int(cac_chu_so[1]) * 10 + int(cac_chu_so[3])
        
        return so_thu_nhat + so_thu_hai