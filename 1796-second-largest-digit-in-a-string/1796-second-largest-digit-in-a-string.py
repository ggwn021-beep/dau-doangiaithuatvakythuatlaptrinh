class Solution(object):
    def secondHighest(self, s):
        quan_quan = -1
        a_quan = -1
        
        for ky_tu in s:
            # Lọc chỉ lấy chữ số (thông qua mã ASCII dưới nền)
            if ky_tu.isdigit():
                so = int(ky_tu)
                
                # Cập nhật Bảng xếp hạng
                if so > quan_quan:
                    # Á quân nhận lại chức của Quán quân cũ
                    a_quan = quan_quan
                    # Quán quân mới đăng quang
                    quan_quan = so
                # Nếu số này bé hơn Quán quân, nhưng lại lớn hơn Á quân cũ
                elif so < quan_quan and so > a_quan:
                    a_quan = so
                    
        return a_quan