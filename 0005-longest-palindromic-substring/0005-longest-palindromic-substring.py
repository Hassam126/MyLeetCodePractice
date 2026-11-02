class Solution(object):
    def longestPalindrome(self, s):
      self.s = s
      c = 0
      r = 2
      l = 0
      li = []

      while c < len(self.s):

        li.append(self.s[c])

        while l>=0 and r<len(self.s):
          if self.s[r] == self.s[l]:
            li.append(self.s[l:r+1])
            l -= 1
            r  += 1
          else:
           break
    
        l = c
        r = c+1

        while( l>=0 and r<len(self.s) ):
          if self.s[r] == self.s[l]:
            li.append(self.s[l:r+1])
            l -= 1
            r  += 1         
          else:
            break
  
        c += 1
        l = c-1
        r = c + 1

      return max(li , key=len) 