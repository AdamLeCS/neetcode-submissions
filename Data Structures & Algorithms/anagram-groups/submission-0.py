class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word, any anagrams will give the same sort
        # create a dictionary: sorted word -> list of indexes that match
        anagram_dict = {}
        index = 0
        # create the dictionary
        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word not in anagram_dict.keys():
                index_list = [index]
                anagram_dict[sorted_word] = index_list
            else:
                index_list = anagram_dict.get(sorted_word)
                index_list.append(index)
            index += 1
        # create the sublists using the indexes
        sublists = []
        for key in anagram_dict.keys():
            indexes = anagram_dict.get(key)
            sublist = []
            for i in indexes:
                sublist.append(strs[i])
            sublists.append(sublist)
        return sublists
        


        