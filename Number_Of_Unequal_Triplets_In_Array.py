class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count={}
        total=0
        totalaux=0
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            total+=1
        totalaux=total
        total=(totalaux*(totalaux-1)*(totalaux-2))//6
        for i,o in count.items():
            if(o>2):
                total-=(o*(o-1)*(o-2))//6
            if(o>1):
                total-=((totalaux-o)*o*(o-1))//2
        return total
