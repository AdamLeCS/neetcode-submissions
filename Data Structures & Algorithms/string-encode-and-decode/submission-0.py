class Solution:
    # before each word, create some kind of metadata string that tells how many letters to read
    def encode(self, strs: List[str]) -> str:
        encoded_str = "".join(f"*{len(s)}*{s}" for s in strs)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        # parse the string
        strs = []
        index = 0
        while (index < len(s)):
            index += 1
            start_index = index
            # after this while loop, index will be at the *
            while (s[index] != '*'):
                index += 1
            letters = int(s[start_index:index]) # should be the num between *'s
            
            index += 1
            strs.append(s[index:index+letters])
            index += letters
        return strs
            

            
