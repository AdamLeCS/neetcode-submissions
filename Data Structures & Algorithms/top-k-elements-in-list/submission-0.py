class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary of nums and their frequencies
        # sort frequencies, find the top k frequencies
        # create the dictionary as nums -> frequency, then reverse it later
        frequencies = {}
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
        freq_to_num = []
        for num, freq in frequencies.items():
            freq_to_num.append([freq, num])
        freq_to_num.sort()
        k_list = []
        for i in range(1, k+1):
            next_num = freq_to_num[len(freq_to_num) - i][1]
            k_list.append(next_num)
        return k_list