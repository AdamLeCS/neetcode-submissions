class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i, n in enumerate(nums):
            j = i + 1
            k = len(nums) - 1

            # skipping duplicate left values
            if i > 0 and n == nums[i-1]:
                continue
            while (j < k):
                three_sum = n + nums[j] + nums[k]
                if three_sum == 0:
                    triplets.append([n, nums[j], nums[k]])
                    print(i, j, k)
                    temp = nums[j]
                    while nums[j] == temp and j < k:
                        j += 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
            
        return triplets
        