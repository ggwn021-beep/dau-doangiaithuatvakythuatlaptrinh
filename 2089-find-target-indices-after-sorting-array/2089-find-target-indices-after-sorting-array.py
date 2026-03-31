class Solution(object):
    def targetIndices(self, nums, target):
        nho_hon = 0
        bang_nhau = 0
        
        for so in nums:
            if so < target:
                nho_hon += 1
            elif so == target:
                bang_nhau += 1
                
        ket_qua = []
        for i in range(bang_nhau):
            ket_qua.append(nho_hon + i)
            
        return ket_qua