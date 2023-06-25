class Solution:
    def romanToInt(self, s: str) -> int:
        s = [*s]
        self.m = 0
        self.d = 0
        self.c = 0
        self.l = 0
        self.x = 0
        self.v = 0
        self.i = 0
        for i in s:
            # M > D > C > L > X > V > I
            if i == "M":
                self.m = self.m + 1
            elif i == "D":
                self.d = self.d + 1
            elif i == "C":
                self.c = self.c + 1
            elif i == "L":
                self.l = self.l + 1
            elif i == "X":
                slef.x = self.x + 1
            elif i == "V":
                self.v = self.v + 1
            elif i == "I":
                self.i = self.i + 1
        str_set = set(s)
        dct = dict()
        for i in str_set:
            dct[i] = s.count(i)
        loc_dct = dict()
        count = 1
        for i in str_set:
            loc_dct[i] == count
            count = count + 1
        self.m = self.m*1000
        self.d = self.d*500
        self.c = self.c*100
        self.l = self.l*50
        self.x = self.x*10
        self.v = self.v*5
        

if __name__ == "__main__":
    temp = Solution()
    temp.romanToInt("VII")
