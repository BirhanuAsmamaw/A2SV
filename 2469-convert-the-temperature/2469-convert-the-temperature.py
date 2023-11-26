class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kel = celsius + 273.15
        far = celsius * 1.80 + 32
        return [kel, far]