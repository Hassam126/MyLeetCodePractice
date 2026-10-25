class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2): 
                    self.n1 = nums1
                    self.n2 = nums2
                    n3 = self.n1 + self.n2
                    n3.sort()
                    sum = 0
                    l = len(n3)
                    if l%2 == 1:       
                        sum = n3[l//2]
                        return sum
                    else:
                        sum = (n3[l//2-1] + n3[(l//2)])/2.0
                        return sum  