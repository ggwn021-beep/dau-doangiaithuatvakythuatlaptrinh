class Solution(object):
    def destCity(self, paths):
        # 1. Tạo tập hợp (Set) chứa tất cả các thành phố xuất phát
        # Set giúp việc tra cứu siêu nhanh
        thanh_pho_xuat_phat = set()
        for chuyen_bay in paths:
            thanh_pho_xuat_phat.add(chuyen_bay[0])
            
        # 2. Kiểm tra các thành phố đến
        for chuyen_bay in paths:
            thanh_pho_den = chuyen_bay[1]
            # Nếu thành phố đến không nằm trong set
            if thanh_pho_den not in thanh_pho_xuat_phat:
                return thanh_pho_den