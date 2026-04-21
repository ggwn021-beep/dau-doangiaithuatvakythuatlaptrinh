class Solution(object):
    def convertTemperature(self, celsius):
        # Áp dụng chuẩn công thức Toán học
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        
        # Trả về mảng chứa 2 giá trị
        return [kelvin, fahrenheit]