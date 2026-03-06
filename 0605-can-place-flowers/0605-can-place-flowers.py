class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # Chèn thêm 2 số 0 vào hai đầu để dễ xử lý mép
        luong_hoa = [0] + flowerbed + [0]
        
        for i in range(1, len(luong_hoa) - 1):
            # Nếu gặp 3 chậu trống liên tiếp
            if luong_hoa[i-1] == 0 and luong_hoa[i] == 0 and luong_hoa[i+1] == 0:
                luong_hoa[i] = 1  # Trồng hoa vào chậu giữa
                n -= 1            # Giảm số hoa cần trồng đi 1
                
        # Nếu n <= 0 là đã trồng đủ (hoặc dư) số hoa yêu cầu
        return n <= 0