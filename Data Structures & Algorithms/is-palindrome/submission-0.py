class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        pruned_str = []
        for char in t:
            if char in valid_chars:
                pruned_str.append(char)
        start = 0
        end = len(pruned_str) - 1
        while start < end:
            if pruned_str[start] != pruned_str[end]:
                return False
            start += 1
            end -= 1
        return True