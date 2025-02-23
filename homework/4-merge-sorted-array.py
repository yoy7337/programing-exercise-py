# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


from typing import List  # 導入 List 型別提示

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int, nums: List[int]) -> None:
        print(nums1)
        print(nums2)
        """
        加入你的程式碼
        """


nums1 = [1, 2, 3]  # List 初始值
m = 3
nums2 = [2, 5, 6]  # 另一個 List 初始值
n = 3
num = [0, 0 ,0 ,0 ,0 ,0]

solution = Solution()
solution.merge(nums1, m, nums2, n, num)
print(num)  # 輸出: [1, 2, 2, 3, 5, 6]