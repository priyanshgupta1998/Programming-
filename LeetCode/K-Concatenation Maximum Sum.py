
#    https://leetcode.com/contest/weekly-contest-154/problems/k-concatenation-maximum-sum/


Q. Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.




sol:-->

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        if not arr or k==0:
            return 0
        
        #Declare the variable with assign the value
        cum=cummin=cummax=sub=submax=total=ans=0
        
        for i in arr:
            cum+=i
            if cum<cummin:
                cummin=cum
            if cum>cummax:
                cummax=cum
            sub=cum-cummin
            if sub>submax:
                submax=sub
        
        total = cum
        
        if k==1:
            ans=submax
        elif total<=0: 
            ans=max(submax,total-cummin+cummax)
        else:
            ans=max(submax,total-cummin+cummax+total*(k-2))
        
        return ans%(10**9 + 7)
