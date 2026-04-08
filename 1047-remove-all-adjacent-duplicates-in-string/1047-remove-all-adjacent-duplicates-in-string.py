class Solution(object):
    def removeDuplicates(self, s):
        ngan_xep = []
        
        for chu in s:
            # Nếu ngăn xếp có đồ VÀ chữ chuẩn bị nhét vào giống hệt chữ trên đỉnh
            if ngan_xep and ngan_xep[-1] == chu:
                ngan_xep.pop() #Vứt chữ trên đỉnh đi
            else:
                ngan_xep.append(chu) # Không giống thì nhét vào an toàn
                
        # Nối các chữ trong ngăn xếp lại thành chuỗi
        return "".join(ngan_xep)