class Solution:
    def hammingWeight(self, n: int) -> int:
        t=str(bin(n))
        count=0
        for i in t:
            if i=='1':
                count=count+1
        return count