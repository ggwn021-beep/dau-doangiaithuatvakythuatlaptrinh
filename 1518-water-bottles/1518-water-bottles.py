class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        tong_da_uong = numBottles
        vo_chai_hien_co = numBottles
        
        # Cứ khi nào vỏ chai còn đủ để đổi ít nhất 1 chai mới thì cứ đổi
        while vo_chai_hien_co >= numExchange:
            # Đi đổi lấy chai mới
            chai_moi = vo_chai_hien_co // numExchange
            
            # Vỏ chai lẻ tẻ bị tiệm tạp hóa trả lại (không đủ đổi)
            vo_chai_le = vo_chai_hien_co % numExchange
            
            # Uống hết chai mới
            tong_da_uong += chai_moi
            
            # Cầm vỏ của chai mới cộng dồn với vỏ lẻ để chuẩn bị cho đợt đổi sau
            vo_chai_hien_co = chai_moi + vo_chai_le
            
        return tong_da_uong