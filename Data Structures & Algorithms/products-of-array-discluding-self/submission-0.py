class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # simple solution
        total_product = 1
        num_zeroes = 0
        for n in nums:
            if n == 0:
                num_zeroes += 1
                continue
            total_product *= n
        if num_zeroes == 0:
            output = []
            for n in nums:
                output.append(total_product // n)
        elif num_zeroes == 1:
            output = []
            for n in nums:
                if n == 0:
                    output.append(total_product)
                else:
                    output.append(0)
        else:
            output = [0] * len(nums)
        return output
        
