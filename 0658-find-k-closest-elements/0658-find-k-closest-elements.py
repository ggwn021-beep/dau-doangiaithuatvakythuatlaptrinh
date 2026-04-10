class Solution(object):
    def findClosestElements(self, arr, k, x):
        # Ta đi tìm 'vi_tri_bat_dau' của nhóm k phần tử
        trai = 0
        phai = len(arr) - k
        
        while trai < phai:
            giua = trai + (phai - trai) // 2
            
            # Khoảng cách từ số bên TRÁI đến target
            khoang_cach_trai = x - arr[giua]
            # Khoảng cách từ số biên PHẢI (vượt khung 1 ô) đến target
            khoang_cach_phai = arr[giua + k] - x
            
            # Nếu số bên phải gần target hơn số bên trái -> Phải dịch toàn bộ khung sang phải
            if khoang_cach_trai > khoang_cach_phai:
                trai = giua + 1
            else:
                # Nếu số bên trái gần hơn (hoặc bằng nhau) -> Dịch khung sang trái
                phai = giua
                
        # Trả về mảng con từ vị trí bắt đầu
        return arr[trai : trai + k]