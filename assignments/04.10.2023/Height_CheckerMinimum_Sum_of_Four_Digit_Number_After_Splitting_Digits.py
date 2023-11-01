class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(str(num))
        
        digits.sort()
        
        new1 = []
        new2 = []
        
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                new1.append(digit)
            else:
                new2.append(digit)

        new1 = int(''.join(new1))
        new2 = int(''.join(new2))
        
        return new1 + new2
