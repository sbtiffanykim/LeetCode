class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            try:
                nums.remove(val)
            except ValueError:
                continue