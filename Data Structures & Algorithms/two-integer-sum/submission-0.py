class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make map between values and their first index in nums
        # if there are duplicates, only care about first index
        array_dict = {}
        index = 0
        for n in nums:
            if n not in array_dict.keys():
                array_dict[n] = index
            index += 1

        # loop through array again and see where target - index is in the map
        index = 0
        x_index = 0
        for n in nums:
            x = target - n
            if x in array_dict.keys():
                x_index = array_dict.get(x)
                if (x_index != index):
                    break
            index += 1

        return [index, x_index] if index < x_index else [x_index, index]