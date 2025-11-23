
"""
Understanding Maximum Consecutive Ones Problem
You are given a binary array, an array consisting only of 0s and 1s. Your task is to find the maximum number of consecutive 1s present in the array.

Example 1
Input: nums = [1, 1, 0, 1, 1, 1]
We can see that:

The first two 1s are followed by a 0.
After that, there are three consecutive 1s.
Output: 3
The maximum number of continuous 1s is 3.

Example 2
Input: nums = [1, 0, 1, 1, 0, 1]
In this case:

There are no more than two 1’s in a row anywhere.
Output: 2
The best streak of 1s is [1, 1], so the result is 2.

Example 3
Input: nums = [0, 0, 0, 0]
Since there are no 1s at all, there’s no sequence to count.

Output: 0
"""


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
        
""" Step-by-Step code Explanation
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

"""



Time and Space Complexity

Time Complexity: O(n):
The function traverses the array nums exactly once.
All operations within the loop (if checks, increments, and max comparisons) are constant-time operations.
Therefore, the time complexity scales linearly with the size of the input array.

Space Complexity: O(1):
The function uses a fixed amount of additional space regardless of the input size.
Variables like cnt and maxi consume constant space.
No additional data structures are used that scale with input size."""
