class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "CD": 400,
            "CM": 900,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }
        k=0
        c=0
        for i in range(0,len(s)):
            if dic.keys().__contains__(s[k:k+2]):
                c+=dic[s[k:k+2]]
                k+=2
            elif len(s)<=k:
                break
            else :
                c+=dic[s[k]]
                k+=1
        return c