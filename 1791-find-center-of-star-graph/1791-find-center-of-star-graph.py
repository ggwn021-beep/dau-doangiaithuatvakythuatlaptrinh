class Solution(object):
    def findCenter(self, edges):
        # Lấy ra 2 cạnh đầu tiên
        canh_1 = edges[0]
        canh_2 = edges[1]
        
        # Nếu điểm đầu của cạnh 1 xuất hiện trong cạnh 2 -> Nó là tâm
        if canh_1[0] in canh_2:
            return canh_1[0]
        # Nếu không, điểm cuối của cạnh 1 chắc chắn là tâm
        else:
            return canh_1[1]