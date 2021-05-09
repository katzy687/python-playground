# BRUTE FORCE
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     return [i, j]

# COMPLEMENT MAP
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num in complement_map:
                return [complement_map[num], i]
            else:
                complement_map[complement] = i


if __name__ == "__main__":
    nums = [11, 15, 2, 7]
    target = 9
    """
    return [0, 1]
    """

    sol = Solution()
    print(sol.twoSum(nums, target))