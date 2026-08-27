class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # add letters and their counts from first word to dictionary
        letters = {}
        for letter in s:
            if letter not in letters.keys():
                letters[letter] = 1
            else:
                letters[letter] += 1
        # decrement letters from second word
        for letter in t:
            if letter not in letters.keys():
                return False
            else:
                letters[letter] -= 1
        # check if any values aren't 0
        for key in letters.keys():
            if letters[key] != 0:
                return False
        return True
        