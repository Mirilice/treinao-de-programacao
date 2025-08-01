class Solution(object):
    def intToRoman(self, num):
        result = ""
        digits = [1000, 500, 100, 50, 10, 5, 1]
        romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        arr = []
        for d in digits:
            if d <= num:
                arr.append(num//d)
                num = num%d
            else: arr.append(0)
        for i in range(len(arr)):
            if arr[i] != 0:
                if arr[i] > 3:
                    value = arr[i-1]*digits[i-1] + arr[i]*digits[i]
                    targNum = value + digits[i]
                    index = digits.index(targNum)
                    if value % 9 == 0: result = result[:-1]
                    result += romans[i] + romans[index]
                else: result+= romans[i]*arr[i]
        return result