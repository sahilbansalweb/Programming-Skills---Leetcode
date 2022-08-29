import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=[int(a) for a in str(n)]
        r1=math.prod(x)
        r2=sum(x)
        return r1-r2        