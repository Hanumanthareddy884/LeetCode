class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        removed_whitespace = s.strip()
        converted_lst = removed_whitespace.split(" ")
        return len(converted_lst[-1])
        