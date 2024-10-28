class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numCount = collections.defaultdict(int)
        for num in nums: 
            if numCount[num] == 1:  # if the num already exist
                return num
            numCount[num] += 1
        