class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        # Từ điển ánh xạ Rule thành vị trí Cột (Index)
        ban_do_cot = {"type": 0, "color": 1, "name": 2}
        cot_can_tim = ban_do_cot[ruleKey]
        
        dem = 0
        for mon_do in items:
            # Truy cập trực tiếp vào cột bằng Index (tốc độ ánh sáng O(1) ở RAM)
            if mon_do[cot_can_tim] == ruleValue:
                dem += 1
                
        return dem