class Solution:

 def twoSum(self,li,target):
    seen = {}

    for i, num in enumerate(li):
         need = target - num
         if need in seen:
            return (list((seen[need] , i)))
        
         seen[num] = i

