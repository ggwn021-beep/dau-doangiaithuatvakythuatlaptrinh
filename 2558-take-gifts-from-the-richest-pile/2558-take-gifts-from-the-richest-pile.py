import heapq
import math

class Solution(object):
    def pickGifts(self, gifts, k):
        # Mặc định heapq của Python là Min-Heap (số nhỏ nổi lên trên)
        # Muốn làm Max-Heap (số to nổi lên trên), ta phải đảo ngược dấu thành số ÂM
        max_heap = [-qua for qua in gifts]
        heapq.heapify(max_heap) # Biến mảng thành cây Heap (O(N))
        
        for _ in range(k):
            # Lấy đống quà to nhất ra and đổi lại dấu dương
            dong_to_nhat = -heapq.heappop(max_heap)
            
            # Tính số quà còn lại (lấy căn bậc hai và làm tròn xuống)
            qua_con_lai = int(math.sqrt(dong_to_nhat))
            
            # Nhét lại đống quà mới vào cây Heap and đổi thành âm
            heapq.heappush(max_heap, -qua_con_lai)
            
        # Cuối cùng, tổng số quà còn lại and đảo ngược dấu âm thành dương
        return sum(-qua for qua in max_heap)