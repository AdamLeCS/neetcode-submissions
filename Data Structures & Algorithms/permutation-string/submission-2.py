class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sort_s1 = "".join(sorted(s1))
        for i in range(len(s2) - len(s1) + 1):
            substr = s2[i : i + len(s1)]
            substr = "".join(sorted(substr))
            if substr == sort_s1:
                return True
        return False
        