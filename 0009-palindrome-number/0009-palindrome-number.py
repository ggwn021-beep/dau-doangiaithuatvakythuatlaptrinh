class Solution(object):
    def isPalindrome(self, x):
        # Số âm HOẶC số tận cùng là 0 (mà khác 0) thì không bao giờ đối xứng
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        nua_dao_nguoc = 0
        
        # Cắt dần nửa sau và lật ngược, đến khi vượt qua nửa trước thì dừng
        while x > nua_dao_nguoc:
            chu_so_cuoi = x % 10
            nua_dao_nguoc = nua_dao_nguoc * 10 + chu_so_cuoi
            x //= 10
            
        # x == nua_dao_nguoc (cho số có chữ số chẵn, VD: 1221 -> x=12, dao=12)
        # x == nua_dao_nguoc // 10 (cho số lẻ chữ số, VD: 12321 -> x=12, dao=123 -> bỏ số 3 ở giữa đi)
        return x == nua_dao_nguoc or x == nua_dao_nguoc // 10