class Solution:
    def trap(self, height: List[int]) -> int:
        left_list = []
        top_height = 0
        for n in height:
            if n > top_height:
                top_height = n
            left_list.append(top_height-n)
        right_list = []
        top_height = 0
        for n in reversed(height):
            if n > top_height:
                top_height = n
            right_list.append(top_height-n)

        # reverse right list
        # note: using insert instead of append actually turns the algo
        # into n^2, so append and reverse after
        right_list.reverse()
        sum = 0
        for i in range(len(height)):
            sum += min(left_list[i], right_list[i])
        return sum
