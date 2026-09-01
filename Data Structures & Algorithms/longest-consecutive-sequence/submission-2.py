class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add each element to a set. Then, go through each num and see if the num right before
        # is in the set -> if it is, add it to another set that tracks starts of sequences
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        unique_nums = set()
        for n in nums:
            unique_nums.add(n)
        
        sequence_starters = []
        for n in unique_nums:
            if (n-1) not in unique_nums:
                sequence_starters.append(n)
        
        max_sequence = 1
        for n in sequence_starters:
            target = n+1
            curr_sequence = 1
            while target in unique_nums:
                target += 1
                curr_sequence += 1
            max_sequence = max(curr_sequence, max_sequence)
            

        return max_sequence


