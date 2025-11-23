""" Step-by-Step Explanation
Initialization:
cnt (Counter):
Keeps track of the current number of consecutive 1s you’ve encountered.
maxi (Maximum):
Records the maximum number of consecutive 1s found so far.
Traversal:
Iterate through each element in nums:
If the current element is 1:
Increment cnt by 1, indicating you’re in a streak of 1s.
If the current element is 0:
Compare cnt with maxi. If cnt is greater, update maxi.
Reset cnt to 0, as the streak has been interrupted by a 0.
Final Comparison:
After traversing the entire array, there might be a streak of 1s that wasn’t followed by a 0. Therefore, perform one final comparison between cnt and maxi to ensure the longest streak is captured.
Result:
Return the value of maxi, which now holds the length of the longest consecutive 1s in the array."""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                maxi = max(maxi, cnt)
                cnt = 0
        return max(maxi, cnt)
        
