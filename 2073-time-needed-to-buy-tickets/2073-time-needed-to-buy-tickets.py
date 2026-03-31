class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        thoi_gian = 0
        ve_cua_toi = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                thoi_gian += min(tickets[i], ve_cua_toi)
            else:
                thoi_gian += min(tickets[i], ve_cua_toi - 1)
                
        return thoi_gian