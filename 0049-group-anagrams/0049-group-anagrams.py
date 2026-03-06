import collections

class Solution(object):
    def groupAnagrams(self, strs):
        # Tạo một cái tủ gồm nhiều ngăn kéo trống
        tu_do = collections.defaultdict(list)
        
        for tu in strs:
            # Rút các chữ cái ra xếp thứ tự lại làm cái "nhãn dán" (ví dụ: 'aet')
            nhan_dan = tuple(sorted(tu))
            
            # Quăng từ hiện tại vào ngăn kéo có cái nhãn dán đó
            tu_do[nhan_dan].append(tu)
            
        # Gom tất cả đồ trong các ngăn kéo ra để trả về
        return list(tu_do.values())