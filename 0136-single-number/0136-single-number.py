class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        non_duplicate = []
        duplicate = []
        for i in nums:
            if i not in non_duplicate:
                non_duplicate.append(i)
            else:
                duplicate.append(i)
        for j in non_duplicate:
            if j not in duplicate:
                return j