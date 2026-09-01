class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add each element to a set. Then, go through each num and see if the num right before
        # is in the set -> if it is, add it to another set that tracks starts of sequences
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        unique_nums = {}
        for n in nums:
            unique_nums[n] = 0
        
        sequence_starters = []
        for n in unique_nums.keys():
            if (n-1) not in unique_nums.keys():
                sequence_starters.append(n)
        
        max_sequence = 1
        for n in sequence_starters:
            target = n+1
            curr_sequence = 1
            while target in unique_nums.keys():
                target += 1
                curr_sequence += 1
            if curr_sequence > max_sequence:
                max_sequence = curr_sequence

        return max_sequence


