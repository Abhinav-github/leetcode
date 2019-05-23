#Given a non negative integer number num. For every numbers i in 
#the range 0 ≤ i ≤ num calculate the number of 1's in their binary 
#representation and return them as an array.

class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = [0]
        for i in range(1,num+1):
            ret.append(ret[i>>1] + (i&1))
        return ret
