class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        non_duplicate = {'non':[],'ori':[]}
        for i in nums:
            if i not in non_duplicate['non']:
                non_duplicate['non'].append(i)
            else:
                non_duplicate['ori'].append(i)
        for j in non_duplicate['non']:
            if j not in non_duplicate['ori']:
                return j