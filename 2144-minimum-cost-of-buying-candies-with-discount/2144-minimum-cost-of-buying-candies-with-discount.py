class Solution(object):
    def minimumCost(self, cost):
        # Sắp xếp giá kẹo từ Đắt nhất xuống Rẻ nhất
        cost.sort(reverse=True)
        
        tong_tien = 0
        for i in range(len(cost)):
            # Cứ đứng ở vị trí thứ 3 (index 2, 5, 8...) là được miễn phí
            if i % 3 != 2:
                tong_tien += cost[i]
                
        return tong_tien