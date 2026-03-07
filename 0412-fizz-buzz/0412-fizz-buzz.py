class Solution(object):
    def fizzBuzz(self, n):
        ket_qua = []
        
        for i in range(1, n + 1):
            # Luôn xét điều kiện gộp (khó nhất) đầu tiên
            if i % 3 == 0 and i % 5 == 0:
                ket_qua.append("FizzBuzz")
            elif i % 3 == 0:
                ket_qua.append("Fizz")
            elif i % 5 == 0:
                ket_qua.append("Buzz")
            else:
                ket_qua.append(str(i)) # Không dính cái nào thì đọc số bình thường
                
        return ket_qua