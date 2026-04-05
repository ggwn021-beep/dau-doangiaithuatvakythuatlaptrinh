class Solution(object):
    def numRescueBoats(self, people, limit):
        # Sắp xếp từ gầy đến béo
        people.sort()
        
        trai = 0
        phai = len(people) - 1
        so_thuyen = 0
        
        while trai <= phai:
            # Nếu người gầy nhất + béo nhất <= limit -> Đi chung
            if people[trai] + people[phai] <= limit:
                trai += 1  # Người gầy đã lên thuyền
                phai -= 1  # Người béo đã lên thuyền
            else:
                # Người béo đi 1 mình, người gầy ở lại
                phai -= 1
                
            # Dù đi chung hay đi 1 mình thì cũng tốn 1 chiếc thuyền
            so_thuyen += 1
            
        return so_thuyen