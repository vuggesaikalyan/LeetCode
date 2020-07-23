class Solution:
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        solution = []
        for i in range(0, nRows):
            count = i
            step1 = 2*(nRows-1-i)
            step2 = 2*i
            while count < len(s):
                solution.append(s[count])
                if step1 > 0 and step2 > 0 and count+step1<len(s):
                    count += step1
                    solution.append(s[count])
                    count += step2
                else:
                    count +=(step1+step2)
        return "".join(solution)