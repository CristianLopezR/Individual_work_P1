class Solution:
  def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
    diff=[]
    for i in range(len(nums)):
      diff.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
    return diff
